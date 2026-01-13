from django.contrib import admin
from .models import ExternalApp

@admin.register(ExternalApp)
class ExternalAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('order', 'is_active')
