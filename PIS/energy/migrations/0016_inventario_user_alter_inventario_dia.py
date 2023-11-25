# Generated by Django 4.2.7 on 2023-11-23 21:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('energy', '0015_alter_inventario_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventario',
            name='dia',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 16, 20, 31, 481004)),
        ),
    ]
