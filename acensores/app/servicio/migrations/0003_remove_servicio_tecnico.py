# Generated by Django 2.1.2 on 2018-12-04 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20181128_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='tecnico',
        ),
    ]
