from django.contrib import admin

from locations.models import Location, Rating

admin.site.register(Location)
admin.site.register(Rating)