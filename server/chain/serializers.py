from rest_framework import serializers

from models import Chain


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = ('name', 'chain_code', 'email',)

