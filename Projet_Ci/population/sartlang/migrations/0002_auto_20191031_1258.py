# Generated by Django 2.2.6 on 2019-10-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sartlang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='population',
            name='nbabts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
