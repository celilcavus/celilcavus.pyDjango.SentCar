from django.contrib import admin

from about import models

# Register your models here.
@admin.register(models.AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id","title")