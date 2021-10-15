# Generated by Django 3.2.6 on 2021-09-09 05:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_whatchlist_auction_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
