from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import QRCodeData

@admin.register(QRCodeData)
class QRCodeDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at')
