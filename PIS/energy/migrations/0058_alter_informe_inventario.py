# Generated by Django 4.2.7 on 2023-12-14 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("energy", "0057_alter_informe_dia_alter_informe_inventario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="informe",
            name="inventario",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inventario",
                to="energy.inventario",
            ),
        ),
    ]
