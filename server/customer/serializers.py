from rest_framework import serializers

from models import Customer
from chain.models import Chain

class ChainCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = ('name',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'number', 'email')


class CustomerChainSerializer(serializers.ModelSerializer):
    chains = ChainCustomerSerializer(read_only=True, many=True)
    class Meta:
        model = Customer
        fields = ('name', 'number', 'chains')
