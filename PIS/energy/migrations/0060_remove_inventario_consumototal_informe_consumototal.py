# Generated by Django 4.2.7 on 2023-12-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("energy", "0059_remove_informe_consumototal"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventario",
            name="consumoTotal",
        ),
        migrations.AddField(
            model_name="informe",
            name="consumoTotal",
            field=models.FloatField(default=0),
        ),
    ]