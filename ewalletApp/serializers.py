from djoser import serializers

from ewalletApp.models import Transaction, Wallet


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction

    fields = ['type', 'status', 'datetime', 'amount', 'wallet', 'pk_reference_number']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet

    fields = ['user', 'balance', 'wallet_number']



