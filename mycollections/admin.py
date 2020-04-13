from django.contrib import admin
from .models import Mycollections


@admin.register(Mycollections)
class MycollectionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
