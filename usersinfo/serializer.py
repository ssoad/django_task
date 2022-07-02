from rest_framework import serializers
from django.contrib.auth.models import User
from usersinfo.models import Customer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    # sender = UserSerializer(read_only=True)
    # receiver = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['phone']