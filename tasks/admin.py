from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'types_ads', 'category_ads', 'format_ads', 'overview')
    search_fields = ('title', 'overview', 'description')
