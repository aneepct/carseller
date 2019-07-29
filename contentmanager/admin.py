from django.contrib import admin

# Register your models here.
from .models import (City, HomepageContent, StepOne, StepTwo, StepThree, CityPage)


class CityAdmin(admin.ModelAdmin):
    model = City


class HomepageContentAdmin(admin.ModelAdmin):
    model = HomepageContent


class StepOneAdmin(admin.ModelAdmin):
    model = StepOne


class StepTwoAdmin(admin.ModelAdmin):
    model = StepTwo


class StepThreeAdmin(admin.ModelAdmin):
    model = StepThree


class CityPageAdmin(admin.ModelAdmin):
    model = CityPage


admin.site.register(City, CityAdmin)
admin.site.register(HomepageContent, HomepageContentAdmin)
admin.site.register(StepOne, StepOneAdmin)
admin.site.register(StepTwo, StepTwoAdmin)
admin.site.register(StepThree, StepThreeAdmin)
admin.site.register(CityPage, CityPageAdmin)
