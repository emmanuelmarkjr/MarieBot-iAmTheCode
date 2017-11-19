# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Question, DangerAlert

# Register your models here.


class DangerAlertAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DangerAlert._meta.fields if field.name != "id"]


admin.site.register(Question)
admin.site.register(DangerAlert, DangerAlertAdmin)