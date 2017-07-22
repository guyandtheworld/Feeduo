from rest_framework import serializers

from models import Chain


class ChainSerializer(serializers.Serializer):
    class Meta:
        model = Chain
        fields = ('name', 'chain_code', 'email',)

class ChainRegistrationSerializer(serializers.ModelSerializer):
    chain_code = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    comfirm_password = serializers.CharField(max_length=30)
    address = serializers.CharField()
    contact_number = serializers.CharField(max_length=10)
    number_of_stores = serializers.IntegerField()

    class Meta:
        model = Chain
        field = "__all__"

    def validate_email(self, email):
        existing = Chain.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("A Chain with that email "
                "address has already registered. Was it you?")
        return email

    def validate_chain_code(self, chain_code):
        existing = Chain.objects.filter(chain_code=chain_code).first()
        if existing:
            raise serializers.ValidationError("A Chain with that chain_code "
                "has been already registered. Was it you?")
        return chain_code

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")

        return data