# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]