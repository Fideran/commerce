# Generated by Django 3.2.6 on 2021-09-01 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_whatchlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatchlist',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Watch_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
