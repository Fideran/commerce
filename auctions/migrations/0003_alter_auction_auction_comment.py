# Generated by Django 3.2.6 on 2021-08-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_comment',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
