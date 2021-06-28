# Generated by Django 3.2.4 on 2021-06-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPayment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='adress',
            field=models.CharField(blank=True, max_length=200, verbose_name='Full Address'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='city',
            field=models.CharField(blank=True, max_length=40, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='country',
            field=models.CharField(blank=True, max_length=40, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, verbose_name='Area Zip Code'),
        ),
    ]
