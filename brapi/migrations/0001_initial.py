# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.CharField(blank=True, default='', max_length=100)),
                ('datatypes', models.CharField(blank=True, default='', max_length=100)),
                ('methods', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]