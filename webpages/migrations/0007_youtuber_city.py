# Generated by Django 3.1.4 on 2020-12-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_auto_20201208_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
