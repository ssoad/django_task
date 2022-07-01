from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from usersinfo.models import Customer
from .models import Transaction
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TransactionView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # global serializer
        token = self.request.headers.get('Authorization')
        print("TOKEN::", token)
        try:
            # token_obj = SMSVerification.objects.get(session_token=token)
            # mobile = token_obj.phone_number
            client = Customer.objects.get(user= request.user)
            send_money = Transaction.objects.filter(sender=client)
            rec_money = Transaction.objects.filter(receiver=client)
            result = send_money | rec_money
            print(result)
            serializer = TransactionSerializer(result, many=True, required=False)
            return Response(serializer.data)
        except:
            return Response({"error": "not found"})

# class TestClass(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         return Response({"message": "Hello World"})