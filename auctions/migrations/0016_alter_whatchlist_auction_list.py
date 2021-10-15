# Generated by Django 3.2.6 on 2021-09-08 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_alter_whatchlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatchlist',
            name='auction_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='auction_lists', to='auctions.auction'),
        ),
    ]