from django.contrib import admin
from .models import Mymessages


@admin.register(Mymessages)
class MymessagesAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
