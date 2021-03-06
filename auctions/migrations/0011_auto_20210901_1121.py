# Generated by Django 3.2.6 on 2021-09-01 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auction_bid_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='bid_user',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.CreateModel(
            name='WhatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_list', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
            ],
        ),
    ]
