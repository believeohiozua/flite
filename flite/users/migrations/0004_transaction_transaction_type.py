# Generated by Django 2.1.9 on 2021-06-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210603_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('p2ptransfer', 'P2PTransfer'), ('banktransfer', 'BankTransfer'), ('Card', 'Card'), ('withdrawal', 'withdrawal')], help_text='mode of transaction', max_length=15, null=True),
        ),
    ]
