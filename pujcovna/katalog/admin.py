from django.contrib import admin

from . import models
admin.site.register(models.Auto)
admin.site.register(models.Vypujcka)
admin.site.register(models.Zakaznik)
admin.site.register(models.FormularAuto)
admin.site.register(models.FormularVypujcka)