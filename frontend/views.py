from django.shortcuts import render

from django.http import JsonResponse
from django.core import serializers
from contentmanager.models import (
    HomepageContent, StepOne, StepTwo, StepThree, City)
from .models import CarBrand, CarModel, CarYear


def index(request):
    city = City.objects.get(name="default")
    car_brands = CarBrand.objects.all()
    homepage_content = HomepageContent.objects.filter(city=city)
    context = {
        "homepage_content": homepage_content,
        "car_brands": car_brands
    }

    return render(request, 'templates/frontend/dashboard.html', context)


def get_car_models(request, car_brand_id):
    car_models = CarModel.objects.all().filter(car_brand_id=car_brand_id)
    return JsonResponse(serializers.serialize("json", car_models), safe=False)


def get_car_years(request, car_model_id):
    car_years = CarYear.objects.filter(car_model_id=car_model_id)
    return JsonResponse(serializers.serialize("json", car_years), safe=False)


def step_one(request):
    city = City.objects.get(name="default")
    car_brands = CarBrand.objects.all()
    stepone_content = StepOne.objects.filter(city=city)
    context = {
        "stepone_content": stepone_content,
        "car_brands": car_brands
    }

    return render(request, 'templates/frontend/step1.html', context)


def step_two(request):
    city = City.objects.get(name="default")
    car_brands = CarBrand.objects.all()
    steptwo_content = StepTwo.objects.filter(city=city)
    context = {
        "steptwo_content": steptwo_content,
        "car_brands": car_brands
    }

    return render(request, 'templates/frontend/step2.html', context)


def step_three(request):
    city = City.objects.get(name="default")
    car_brands = CarBrand.objects.all()
    stepthree_content = StepThree.objects.filter(city=city)
    context = {
        "stepthree_content": stepthree_content,
        "car_brands": car_brands
    }

    return render(request, 'templates/frontend/step3.html', context)
