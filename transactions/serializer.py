from rest_framework import serializers

class MoneyTransferSerializer(serializers.ModelSerializer):
    sender = CustomerSerializer(read_only=True)

    class Meta:
        model = MoneyTransfer
        fields = '__all__'