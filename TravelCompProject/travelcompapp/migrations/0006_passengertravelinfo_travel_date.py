# Generated by Django 3.1.3 on 2020-11-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelcompapp', '0005_auto_20201127_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengertravelinfo',
            name='travel_date',
            field=models.DateField(default=None),
        ),
    ]
