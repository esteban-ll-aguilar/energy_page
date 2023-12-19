# Generated by Django 4.2.7 on 2023-12-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("energy", "0048_remove_informe_inventario_inventario_informe"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artefactos",
            name="inventario",
        ),
        migrations.RemoveField(
            model_name="inventario",
            name="informe",
        ),
        migrations.AddField(
            model_name="informe",
            name="inventario",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inventario",
                to="energy.inventario",
            ),
        ),
        migrations.AddField(
            model_name="inventario",
            name="artefacto",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="artefactoList",
                to="energy.artefactos",
            ),
        ),
    ]