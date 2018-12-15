# Generated by Django 2.1.2 on 2018-11-23 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombreEmpresa', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('horaInicio', models.DateTimeField()),
                ('horaTermino', models.DateTimeField()),
                ('IdAscensor', models.CharField(max_length=50)),
                ('modeloAcensor', models.CharField(max_length=50)),
                ('fallas', models.TextField()),
                ('reparaciones', models.TextField()),
                ('piezasCambiadas', models.TextField()),
                ('nombreTecnico', models.CharField(max_length=50)),
            ],
        ),
    ]