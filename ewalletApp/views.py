from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from ewalletApp.models import Wallet, Transaction, User
from ewalletApp.serializers import WalletSerializer, TransactionSerializer, UserSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

