import uuid
from rest_framework import serializers
from .models import Transaction
from usersinfo.serializer import CustomerSerializer

class TransactionSerializer(serializers.ModelSerializer):
    # sender = CustomerSerializer()
    # receiver = CustomerSerializer(read_only=True)
    # tran_id = serializers.SerializerMethodField('get_trans_id')

    class Meta:
        model = Transaction
        fields = '__all__'
    
    # def get_trans_id(self,obj):
    #     trn_id = uuid.uuid4().hex[:11].upper()
    #     return trn_id