# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180717_0914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expense',
            new_name='Expenses',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
