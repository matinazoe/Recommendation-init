# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date updated'),
        ),
    ]
