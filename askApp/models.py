# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    answer = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.answer


class DangerAlert(models.Model):
    alert_address = models.CharField(max_length=255)
    alert_attended_to = models.BooleanField(default=False)
    alert_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alert_address
