from django.contrib import admin
from .models import Mytools


@admin.register(Mytools)
class MytoolsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
