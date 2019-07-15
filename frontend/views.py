import json

from django.shortcuts import (render, HttpResponseRedirect, HttpResponse)
from rest_framework import serializers
from django.core.mail import EmailMessage
from django.template.loader import get_template

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



def update_session_city(request):
    city_session = request.POST['city_name']

    if request.session.get('city_id', False):
        response = False

    else:
        try:
            city = City.objects.get(name=city_session)
            request.session['city_id'] = city.id
            response = True

        except City.DoesNotExist:
            response = False

    return HttpResponse(response)


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
            "car_brands": car_brands,
            "car_brand": car_data['car_brand'],
            "car_model": car_data['car_model'],
            "car_year": car_data['car_year']
        }

        return render(request, 'templates/frontend/step1.html', context)

    else:
        return HttpResponseRedirect("/")

def step_two(request):
    car_data = request.POST
    city = City.objects.get(name="default")
    car_brands = CarBrand.objects.all()
    steptwo_content = StepTwo.objects.filter(city=city)
    car_session_data = {
        "car_brand": car_data['car_brand'],
        "car_model": car_data['car_model'],
        "car_year": car_data['car_year']
    }

    car_session_store_data = {
        "car_brand": car_data['car_brand_name'],
        "car_model": car_data['car_model_name'],
        "car_year": car_data['car_year_name']
    }

    request.session['car_store_data'] = car_session_store_data

    request.session['car_data'] = car_session_data

    context = {
        "steptwo_content": steptwo_content,
        "car_brands": car_brands,
        "car_data": request.session['car_data']
    }

    return render(request, 'templates/frontend/step2.html', context)


def step_three(request):
    car_data = request.POST
    car_session_data = request.session['car_data']
    car_session_store_data  = request.session['car_store_data']

    step_two_car_session_data = {
        "car_brand": car_session_data['car_brand'],
        "car_model": car_session_data['car_model'],
        "car_year": car_session_data['car_year'],
        "car_type": car_data['car_type'],
        "car_body_type": car_data['car_body_type'],
        "car_body_sub_type": car_data['car_body_sub_type'],
        "kilometer": car_data['kilometer'],
        "user_email": car_data['user_email'],
        "vehicle_type": car_data['vehicle_type'],
        "user_message": car_data['user_message']
    }

    step_two_car_store_data = {
        "car_brand": car_session_store_data['car_brand'],
        "car_model": car_session_store_data['car_model'],
        "car_year": car_session_store_data['car_year'],
        "car_type": car_data['car_type_name'],
        "car_body_type": car_data['car_body_type_name'],
        "car_body_sub_type": car_data['car_body_sub_type_name'],
        "kilometer": car_data['kilometer'],
        "user_email": car_data['user_email'],
        "vehicle_type": car_data['vehicle_type'],
        "user_message": car_data['user_message']
    }

    request.session['car_data'] = step_two_car_session_data
    request.session['car_store_data'] = step_two_car_store_data

    city = City.objects.get(name="default")
    car_brands = CarBrand.objects.all()
    stepthree_content = StepThree.objects.filter(city=city)
    context = {
        "stepthree_content": stepthree_content,
        "car_brands": car_brands
    }

    return render(request, 'templates/frontend/step3.html', context)


def submit_request(request):
    step_three_data = request.POST
    step_two_car_store_data = request.session['car_store_data']

    to = ['support@gebrauchtauto-ankauf.de']
    subject = 'Customer contact Request'
    from_email = step_two_car_store_data['user_email']

    ctx = {
        'step_three_data': step_three_data,
        'step_two_car_store_data': step_two_car_store_data
    }

    message = get_template(
        'templates/frontend/email/customer_contact.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    cust_msg = EmailMessage(
        'Your Contact Request',
        'Your constact Request have been submitted please wait for response.',
        to=[step_two_car_store_data['user_email']],
        from_email='support@gebrauchtauto-ankauf.de'
    )
    cust_msg.send()

    request_data = request.POST
    car_session_data = request.session['car_data']
    return JsonResponse({
        "req_data": request_data, "car_data": car_session_data
    }, safe=False)
