# Generated by Django 4.2.7 on 2023-11-23 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0006_alter_inventario_consumototal'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='dia',
            field=models.DateField(blank=True, null=True),
        ),
    ]