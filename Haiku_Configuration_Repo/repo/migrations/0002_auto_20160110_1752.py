# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='is_working',
            field=models.CharField(max_length=10),
        ),
    ]
