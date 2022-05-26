# Generated by Django 3.1.14 on 2022-05-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_auto_20220523_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_caution',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_danger',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_warning',
            field=models.BooleanField(default=0),
        ),
    ]