# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]