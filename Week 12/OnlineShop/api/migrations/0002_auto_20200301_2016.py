# Generated by Django 2.2 on 2020-03-01 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorylist',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categorylist',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='categorylist',
            name='name',
            field=models.CharField(choices=[('home', 'home'), ('School', 'School'), ('Uni', 'Uni'), ('Dorm', 'Dorm')], default='home', max_length=200),
        ),
    ]
