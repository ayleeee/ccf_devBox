# Generated by Django 4.0.4 on 2022-05-06 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ccfApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesystem',
            name='content',
        ),
        migrations.AddField(
            model_name='filesystem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filesystem',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
