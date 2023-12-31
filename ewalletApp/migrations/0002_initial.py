# Generated by Django 4.2.4 on 2023-08-21 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ewalletApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ewalletApp.wallet'),
        ),
    ]
