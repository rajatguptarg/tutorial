# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]