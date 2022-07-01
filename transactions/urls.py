from django.urls import path
from .views import *

urlpatterns = [
    path('history/', TransactionView.as_view(), name='history'),
    path('sendmoney/', SendMoney.as_view(), name='send_money'),

]