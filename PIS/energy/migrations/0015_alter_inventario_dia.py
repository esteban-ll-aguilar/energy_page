# Generated by Django 4.2.7 on 2023-11-23 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0014_alter_inventario_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='dia',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 16, 15, 43, 7762)),
        ),
    ]