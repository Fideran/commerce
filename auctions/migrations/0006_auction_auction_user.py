# Generated by Django 3.2.6 on 2021-08-27 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auction_auction_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auction_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]