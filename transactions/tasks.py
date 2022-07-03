from background_task import background
from .models import Transaction
# Create your views here.

@background(schedule=10)
def complete_transaction(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    client = transaction.sender
    receiver = transaction.receiver
    client.balance = client.balance - float(transaction.amount)
    receiver.balance = receiver.balance + float(transaction.amount)
    client.save()
    receiver.save()
    transaction.is_completed = True
    transaction.save()   
    return print("Success")
