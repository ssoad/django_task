import uuid
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from transactions.serializer import TransactionSerializer
from usersinfo.models import Customer
from .models import Transaction
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# Create your views here.

class TransactionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # global serializer
        try:
            
            client = Customer.objects.get(user= request.user)
            send_money = Transaction.objects.filter(sender=client)
            rec_money = Transaction.objects.filter(receiver=client)
            result = send_money | rec_money
            print(result)
            serializer = TransactionSerializer(result, many=True, required=False)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)



class SendMoney(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            client = Customer.objects.get(user = request.user)
            receiver = Customer.objects.get(phone = request.data['receiver'])
            trn_id = uuid.uuid4().hex[:10].upper()
            money_transfer = Transaction(sender=client, receiver=receiver, amount=request.data['amount'], tran_id=trn_id)
            money_transfer.save()
            client.balance = client.balance - float(request.data['amount'])
            receiver.balance = receiver.balance + float(request.data['amount'])
            client.save()
            receiver.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                        status=HTTP_400_BAD_REQUEST)