# Generated by Django 3.2.4 on 2021-06-26 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPayment', '0003_auto_20210627_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='adress',
            new_name='address',
        ),
    ]