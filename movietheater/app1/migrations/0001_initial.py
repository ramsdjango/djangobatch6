# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieTheater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
            ],
        ),
    ]
