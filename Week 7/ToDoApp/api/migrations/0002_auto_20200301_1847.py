# Generated by Django 2.2 on 2020-03-01 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='status',
            field=models.CharField(choices=[('to do', 'to do'), ('in process', 'in process'), ('done', 'done')], max_length=200),
        ),
    ]
