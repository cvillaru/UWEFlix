# Generated by Django 4.1.6 on 2023-02-27 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UWEFlix', '0003_clubrepresentative'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubrepresentative',
            name='Full Name',
        ),
        migrations.AlterField(
            model_name='clubrepresentative',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]