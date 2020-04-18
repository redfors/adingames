from django.contrib import admin
from .models import TypesAds, Playgrounds, Advertiser, FormatAds, CategoryAds

admin.site.register(Playgrounds)

admin.site.register(TypesAds)

admin.site.register(Advertiser)

admin.site.register(FormatAds)

admin.site.register(CategoryAds)

