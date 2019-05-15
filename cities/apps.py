from django.apps import AppConfig
from django.contrib import admin
from .models import City


class CitiesConfig(AppConfig):
    name = 'cities'


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)


admin.site.register(City, CityAdmin)
