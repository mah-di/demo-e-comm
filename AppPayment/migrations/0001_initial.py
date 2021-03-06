# Generated by Django 3.2.4 on 2021-06-26 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200, verbose_name='Full Address')),
                ('city', models.CharField(max_length=40, verbose_name='City')),
                ('country', models.CharField(max_length=40, verbose_name='Country')),
                ('zipcode', models.CharField(max_length=10, verbose_name='Area Zip Code')),
                ('phone', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
