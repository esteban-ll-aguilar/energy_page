# Generated by Django 4.2.7 on 2024-02-27 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("energy", "0017_alter_artefacto_horas_de_uso"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventario",
            name="cantidad_artefacto",
            field=models.FloatField(),
        ),
    ]
