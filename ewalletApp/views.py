from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from ewalletApp.models import Wallet, Transaction, User
from ewalletApp.serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



