# Generated by Django 5.0.1 on 2024-02-05 06:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_salesorder_datetime_salesorder_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
