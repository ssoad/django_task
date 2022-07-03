from django.db import models
from django.conf import settings
# Create your models here.

class Customer(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=False, null=False, unique=True)
    balance = models.FloatField(default=0)


    def __str__(self):
        return self.phone
