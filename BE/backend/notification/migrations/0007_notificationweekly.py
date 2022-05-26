# Generated by Django 3.1.14 on 2022-05-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_auto_20220526_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationWeekly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('total_hit', models.IntegerField(default=0)),
                ('total_kick', models.IntegerField(default=0)),
                ('total_danger', models.IntegerField(default=0)),
                ('total_warning', models.IntegerField(default=0)),
                ('total_caution', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'notificationWeekly',
            },
        ),
    ]