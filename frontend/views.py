import json

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from rest_framework import serializers

from django.http import JsonResponse
from contentmanager.models import (
    HomepageContent, StepOne, StepTwo, StepThree, City)
from .models import CarBrand, CarModel, CarYear


def read_file(request):
    f = open('/var/www/html/.well-known/pki-validation/2F3200EA6A9E9606DC07BFCC343C8D13.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'car_brand', 'name', 'alias')


class CarYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarYear
        fields = ('id', 'car_model', 'name', 'alias')


def index(request):
    if request.session.get('city_id', False):
        city = City.objects.get(id=request.session['city_id'])
        current_city_location = True
    else:
        city = City.objects.get(name="default")
        current_city_location = False

    cities = City.objects.all()
    car_brands = CarBrand.objects.all()
    homepage_content = HomepageContent.objects.filter(city=city)
    car_data = {}
    if request.session.get('car_data', False):
        car_data = request.session['car_data']

    if not homepage_content:
        city = City.objects.get(name="default")
        homepage_content = HomepageContent.objects.filter(city=city)

    serializer = CitySerializer(cities, many=True)
    context = {
        "homepage_content": homepage_content,
        "car_brands": car_brands,
        "cities": json.dumps(serializer.data),
        "current_city_location": current_city_location,
        "car_session_data": car_data,
    }

    return render(request, 'templates/frontend/dashboard.html', context)


def get_car_models(request, car_brand_id):
    car_models = CarModel.objects.filter(car_brand_id=car_brand_id)
    serializer = CarModelSerializer(car_models, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_car_years(request, car_model_id):
    car_years = CarYear.objects.filter(car_model_id=car_model_id)
    serializer = CarYearSerializer(car_years, many=True)
    return JsonResponse(serializer.data, safe=False)


def update_location_city(request, city_id):
    request.session['city_id'] = city_id
    return HttpResponseRedirect("/")


def step_one(request):
    if request.method == "POST":
        car_data = request.POST
        print(car_data)
        car_session_data = {
            "car_brand": car_data['car_brand'],
            "car_model": car_data['car_model'],
            "car_year": car_data['car_year']
        }

        request.session['car_data'] = car_session_data

        city = City.objects.get(name="default")
        car_brands = CarBrand.objects.all()
        stepone_content = StepOne.objects.filter(city=city)
        context = {
            "stepone_content": stepone_content,
            "car_brands": car_brands
        }

        return render(request, 'templates/frontend/step1.html', context)

    else:
        return HttpResponseRedirect("/")

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
