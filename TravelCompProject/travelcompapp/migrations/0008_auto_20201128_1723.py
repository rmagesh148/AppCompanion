# Generated by Django 3.1.3 on 2020-11-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelcompapp', '0007_auto_20201128_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]