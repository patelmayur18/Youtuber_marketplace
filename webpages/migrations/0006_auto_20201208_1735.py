# Generated by Django 3.1.4 on 2020-12-08 12:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_auto_20201208_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='discription',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
