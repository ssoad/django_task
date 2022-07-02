from rest_framework import serializers
from .models import Transaction
from usersinfo.serializer import CustomerSerializer

class TransactionSerializer(serializers.ModelSerializer):
    sender = CustomerSerializer(read_only=True)
    receiver = CustomerSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'