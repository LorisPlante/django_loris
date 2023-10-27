from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.Articles)
admin.site.register(models.Categories)
admin.site.register(models.Tags)