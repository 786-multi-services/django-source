# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-05 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_auto_20160706_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttoken',
            name='token',
            field=models.CharField(default=b'1C904AB0', editable=False, max_length=8, unique=True),
        ),
    ]