# Generated by Django 4.2.7 on 2024-02-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("energy", "0014_alter_artefacto_consumo_wh"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artefacto",
            name="consumo_wh",
            field=models.PositiveIntegerField(default=0),
        ),
    ]