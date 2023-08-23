from rest_framework import serializers

from ewalletApp.models import Wallet, Transaction
from user.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['email', 'phone_number']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']

