from django.contrib import admin

# Register your models here.
from .models import (CarBrand, CarModel, CarYear)


class CarBrandAdmin(admin.ModelAdmin):
    model = CarBrand


class CarModelAdmin(admin.ModelAdmin):
    model = CarModel


class CarYearAdmin(admin.ModelAdmin):
    model = CarYear


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarYear, CarYearAdmin)
