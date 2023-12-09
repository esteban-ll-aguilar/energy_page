# Generated by Django 4.2.7 on 2023-12-09 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0042_remove_inventario_artefacto_artefactos_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artefactos',
            name='horasDeUso',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artefactos',
            name='inventario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artefsactoList', to='energy.inventario'),
        ),
        migrations.AlterField(
            model_name='informe',
            name='inventario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='energy.inventario'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cantidadArtefactos',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='horasDeUso',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
