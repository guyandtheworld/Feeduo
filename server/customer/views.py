import json

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chain.models import Chain
from customer.models import Customer
from customer.serializers import CustomerSerializer, CustomerChainSerializer, ChainCustomerSerializer


class CustomerList(APIView):
    """
    Create Customer or view all Customers
    """

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
            if chain is not None and chain not in customer.chains.all() :
                customer.chains.add(chain)
                success.append(chain_name)
        success_json = {}
        success_json["added"] = success
        return Response(success_json, status=status.HTTP_201_CREATED)