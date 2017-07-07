import json

from django.http import Http404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chain.models import Chain

from models import Customer
from permissions import IsPostOrIsAuthenticated
from serializers import CustomerSerializer, CustomerChainSerializer, ChainCustomerSerializer

from permissions import IsPostOrIsAuthenticated


"""
Security Issue

The security problem faced now is, suppose a person registers his details name,
email, number on the site which uses no password, a time limit 
is to be set for selecting the chain after the initial log in details.
For adding more chains or changing email or number, one has to got to our site,
get a comfirmation email to their own email and a time limit will be provided for
selecting the chains or to change the number. To change email, one will receive a 
message on their registered number and can use the token or link to change the 

Throttling Issue

Since the API can be very prone to DDoS attacks, we're keeping the throttling value
to the bare minimum. The GET request for Customer and Chain will be accessible to 
only the authorized user and the POST request will be limited to 3 per minute and 10
per day.
"""


class CustomerList(APIView):
    """
    Create Customer or view all Customers
    """

    permission_classes = (IsPostOrIsAuthenticated,)

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Retrieve, update, delete a Customer
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerChainView(APIView):
    """
    Link chains with customer
    Add and view the chains related with Customer
    """

    """
    TODO

    add DELETE UPDATE to CustomerChainView
    """

    def get_customer_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404            

    def get(self, request, pk, format=None):
        customer = self.get_customer_object(pk)
        serializer = CustomerChainSerializer(customer)        
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        customer = self.get_customer_object(pk)
        chains = request.GET.get('chains')
        chains = chains.split(',')
        success = []
        for chain_name in chains:
            try:
                chain = Chain.objects.get(name=chain_name)
            except Chain.DoesNotExist:
                chain = None
            # Inefficient method
            if chain is not None and chain not in customer.chains.all() :
                customer.chains.add(chain)
                success.append(chain_name)
        customer.save()
        success_json = {}
        success_json["added"] = success
        return Response(success_json, status=status.HTTP_201_CREATED)
