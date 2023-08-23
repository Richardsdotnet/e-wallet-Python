from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from ewalletApp.models import Wallet
from user.models import User


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(
            user=instance, wallet_number=instance.phone[1:]
        )
