# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0003_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
