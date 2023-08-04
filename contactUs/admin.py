from django.contrib import admin

from contactUs import models

# Register your models here.
@admin.register(models.ContactModel)
class AdminContact(admin.ModelAdmin):
    list_display = ('id','name','message')