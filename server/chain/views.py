from django.http import Http404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Chain
from serializers import ChainSerializer

from permissions import IsGetOrIsAuthenticated


class ChainList(APIView):
    """
    Create Chain or view all Chains
    """

    permission_classes = (IsGetOrIsAuthenticated,)

    def get(self, request, format=None):
        Chains = Chain.objects.all()
        serializer = ChainSerializer(Chains, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChainDetail(APIView):
    """
    Retrieve, update, delete a Chain
    """

    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Chain.objects.get(pk=pk)
        except Chain.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Chain = self.get_object(pk)
        serializer = ChainSerializer(Chain)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        Chain = self.get_object(pk)
        serializer = ChainSerializer(Chain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Chain = self.get_object(pk)
        Chain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
