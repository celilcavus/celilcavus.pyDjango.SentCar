from django.contrib import admin

from blog import models

# Register your models here.
@admin.register(models.BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id","title","date","description")
    
