import json

from django.http import Http404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chain.models import Chain

from models import Customer
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
            res_data = serializer.data
            pk = Customer.objects.get(number=res_data['number']).pk
            res_data['pk'] = pk
            return Response(res_data, status=status.HTTP_201_CREATED)
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
        chain_code = request.POST.get('chain_code')
        if chain_code == None:
            return Response({"STATUS": "No chains provided"}, status=status.HTTP_206_PARTIAL_CONTENT)
        chain_code = chain_code.split(',')
        success = []
        chains = customer.chains.all()
        for code in chain_code:
            try:
                chain = Chain.objects.get(chain_code=code)
            except Chain.DoesNotExist:
                chain = None
            if chain is not None and chain not in chains:
                customer.chains.add(chain)
                success.append(code)
        customer.save()
        if len(success)>0:
            success_json = {}
            success_json["added"] = success
            return Response(success_json, status=status.HTTP_201_CREATED)
        return Response({"STATUS": "WRONG DETAILS"}, status=status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, request, pk, format=None):
        customer = self.get_customer_object(pk)
        chain_code = request.POST.get('chain_code')
        if chain_code == None:
            return Response({"STATUS": "No chains provided"}, status=status.HTTP_206_PARTIAL_CONTENT)
        chain_code = chain_code.split(',')
        success = []
        chains = customer.chains.all()
        for code in chain_code:
            try:
                chain = Chain.objects.get(chain_code=code)
            except Chain.DoesNotExist:
                chain = None
            if chain is not None and chain in chains:
                customer.chains.remove(chain)
                success.append(code)
        customer.save()
        if len(success)>0:
            success_json = {}
            success_json["removed"] = success
            return Response(success_json, status=status.HTTP_201_CREATED)
        return Response({"STATUS": "WRONG DETAILS"}, status=status.HTTP_206_PARTIAL_CONTENT)
