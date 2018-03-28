# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=40, blank=False)
    password = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=40, blank=False)
    token = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=False)

    class Meta:
        ordering = ('created', )
