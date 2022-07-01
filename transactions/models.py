from django.db import models

from usersinfo.models import Customer

# Create your models here.
class Transaction(models.Model):
    sender = models.ForeignKey(Customer, to_field="user", on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Customer, to_field="user", on_delete=models.CASCADE, related_name="receiver")
    amount = models.FloatField(null=False, blank=False)
    tran_id = models.CharField(max_length=20, unique=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.sender.user.first_name+"-"+self.receiver.user.first_name+":"+str(self.amount))