from datetime import datetime
from functools import partial
import uuid
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize
from django.utils.timezone import make_aware
from transactions.serializer import TransactionSerializer
from transactions.tasks import complete_transaction
from usersinfo.models import Customer
from .models import Transaction
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# from .tasks import background_tasks
# Create your views here.


class TransactionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # global serializer
        try:
            # background_tasks()
            client = Customer.objects.get(user=request.user)
            send_money = Transaction.objects.filter(sender=client)
            rec_money = Transaction.objects.filter(receiver=client)
            result = send_money | rec_money
            # print(result)
            serializer = TransactionSerializer(
                result, many=True, required=False)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)


class SendMoney(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            client = Customer.objects.get(user=request.user)
            receiver = Customer.objects.get(phone=request.data['receiver'])
            date_time = datetime.strptime(request.data['datetime'], '%d/%m/%y %H:%M:%S') #02/07/22 23:56:19
            if client.balance > float(request.data['amount']):
                money_transfer = Transaction(
                    sender=client, receiver=receiver, amount=request.data['amount'], tran_id=uuid.uuid4().hex[:11].upper(), datetime=make_aware(date_time))
                money_transfer.save()
                # print(money_transfer.datetime)
                now = datetime.now(money_transfer.datetime.tzinfo)
                if money_transfer.datetime < now:
                    # print("Transaction is completed")
                    complete_transaction.now(money_transfer.id)
                else:
                    # print("Transaction is not completed")
                    complete_transaction(money_transfer.id, schedule=money_transfer.datetime)
                
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "failure"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)},
                            status=HTTP_400_BAD_REQUEST)
