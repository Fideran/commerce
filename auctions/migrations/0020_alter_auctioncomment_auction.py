# Generated by Django 3.2.6 on 2021-09-10 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auctioncomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioncomment',
            name='auction',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='auctions.auction'),
        ),
    ]
