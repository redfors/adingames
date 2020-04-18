from django.contrib import admin
from .models import Deals
from deals.models import DealManager


@admin.register(DealManager)
class DealManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
