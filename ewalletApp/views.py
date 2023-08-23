# Create your views here.
import uuid
from datetime import datetime

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ewalletApp.models import Wallet, Transaction
from ewalletApp.serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    @action(detail=True, methods=['post'])
    def transfer(self, sender_wallet_number, amount, receiver_wallet_number):
        sender = Wallet.objects.get(pk=sender_wallet_number)
        receiver = Wallet.objects.get(pk=receiver_wallet_number)

        transaction = Transaction.objects.create()
        transaction.transaction_type = 'TRANSFER'
        transaction.date_time = datetime.datetime.now()
        transaction.amount = amount
        transaction.wallet = sender
        transaction.reference_number = uuid.uuid4()

        if sender.balance > amount and sender.balance > 0:
            sender.balance -= amount
            receiver.balance += amount
            transaction.transaction_status = 'SUCCESSFUL'
            transaction.save()
            sender.save()
            receiver.save()

    @action(detail=True, methods=['post'])
    def deposit(self, amount, receiver_wallet_number):
        receiver = Wallet.objects.get(pk=receiver_wallet_number)

        transaction = Transaction.objects.create()
        transaction.transaction_type = 'DEPOSIT'
        transaction.date_time = datetime.datetime.now()
        transaction.amount = amount
        transaction.reference_number = uuid.uuid4()

        receiver.balance += amount
        transaction.transaction_status = 'SUCCESSFUL'
        transaction.save()
        receiver.save()


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
