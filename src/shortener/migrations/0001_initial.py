# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnyzURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com])),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
