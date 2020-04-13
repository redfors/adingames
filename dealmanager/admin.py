from django.contrib import admin
from .models import Dealmanager


@admin.register(Dealmanager)
class DealmanagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
