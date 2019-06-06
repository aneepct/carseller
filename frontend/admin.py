from django.contrib import admin

# Register your models here.
from .models import (
    CarBrand, CarModel, CarYear, CarDesign, CarTrim, CarType)


class CarBrandAdmin(admin.ModelAdmin):
    model = CarBrand


class CarModelAdmin(admin.ModelAdmin):
    model = CarModel


class CarYearAdmin(admin.ModelAdmin):
    model = CarYear


class CarDesignAdmin(admin.ModelAdmin):
    model = CarDesign


class CarTrimAdmin(admin.ModelAdmin):
    model = CarTrim


class CarTypeAdmin(admin.ModelAdmin):
    model = CarType


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarYear, CarYearAdmin)
admin.site.register(CarDesign, CarDesignAdmin)
admin.site.register(CarTrim, CarTrimAdmin)
admin.site.register(CarType, CarTypeAdmin)
