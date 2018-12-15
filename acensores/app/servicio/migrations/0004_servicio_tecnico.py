# Generated by Django 2.1.2 on 2018-12-07 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicio', '0003_remove_servicio_tecnico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='tecnico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
