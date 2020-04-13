from django.contrib import admin
from .models import Newspage


@admin.register(Newspage)
class NewspageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'overview', 'created')
    list_filter = ('title', 'overview')
    search_fields = ('title', 'overview', 'description')
