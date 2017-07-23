from rest_framework import serializers

from models import Chain


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = ('name', 'chain_code', 'email',)


class ChainRegistrationSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(max_length=30, allow_blank=False, write_only=True)
    class Meta:
        model = Chain
        fields = ['chain_code', 'name', 'email', 'address', 'contact_number',
                 'number_of_stores', 'confirm_password']
        write_only_fields = ['password',]

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

    def create(self, validated_data):
        del validated_data["confirm_password"]
        return Chain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.chain_code = validated_data.get('chain_code', instance.content)
        instance.name = validated_data.get('name', instance.content)
        instance.address = validated_data.get('address', instance.content)
        instance.password = validated_data.get('password', instance.content)
        instance.contact_number = validated_data.get('contact_number', instance.content)
        instance.number_of_stores = validated_data.get('number_of_number', instance.content)
        instance.save()
        return instance
