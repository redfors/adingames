from django.contrib import admin
from .models import TypesAds, Playgrounds, Advertiser

admin.site.register(Playgrounds)

admin.site.register(TypesAds)

admin.site.register(Advertiser)