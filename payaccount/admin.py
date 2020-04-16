from django.contrib import admin
from .models import PayAccount


@admin.register(PayAccount)
class PayAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
