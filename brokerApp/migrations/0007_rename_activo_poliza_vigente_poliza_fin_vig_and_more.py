# Generated by Django 4.0.3 on 2022-03-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerApp', '0006_poliza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poliza',
            old_name='activo',
            new_name='vigente',
        ),
        migrations.AddField(
            model_name='poliza',
            name='fin_vig',
            field=models.DateField(blank=True, null=True, verbose_name='Fin de Vigencia'),
        ),
        migrations.AddField(
            model_name='poliza',
            name='ini_vig',
            field=models.DateField(blank=True, null=True, verbose_name='Inicio de Vigencia'),
        ),
    ]
