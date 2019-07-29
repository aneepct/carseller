from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.http import HttpResponseRedirect
from contentmanager.models import (
    HomepageContent, StepOne, StepTwo, StepThree, City)
from frontend.models import (
    CarBrand, CarModel, CarYear, CarDesign, CarTrim, CarType
)


@login_required(login_url='/gadadmin/login')
def index(request):
    return HttpResponseRedirect('/gadadmin/dashboard')


def logout_view(request):
    redirect_to = '/gadadmin/login'
    logout(request)
    return HttpResponseRedirect(redirect_to)


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gadadmin/dashboard')
            else:
                messages.warning(request, 'Your account has been disabled!')
        else:
            messages.error(request, 'Incorrect Username or Password.')
    return render(request, 'templates/gadadmin/login.html')


@login_required(login_url='/gadadmin/login')
def dashboard(request):
    city_count = City.objects.all().count()
    context = {
        "city_count": city_count
    }

    return render(request, 'templates/gadadmin/index.html', context)


@login_required(login_url='/gadadmin/login')
def cities_page(request):
    cities = City.objects.all()

    context = {"cities": cities}
    return render(request, 'templates/gadadmin/cities.html', context)


@login_required(login_url='/gadadmin/login')
def cars_page(request):
    cars = CarBrand.objects.all()

    cars_list = []

    for car in cars:
        car_data = {}
        car_data["brand"] = car.name
        car_data["model"] = car.get_models
        cars_list.append(car_data)

    context = {
        "cars": cars_list
    }

    return render(request, 'templates/gadadmin/cars.html', context)


@login_required(login_url='/gadadmin/login')
def import_cars(request):
    return HttpResponseRedirect("/gadadmin/cars_page")


@login_required(login_url='/gadadmin/login')
def remove_car(request, car_brand_id):
    return HttpResponseRedirect("/gadadmin/cars_page")


@login_required(login_url='/gadadmin/login')
def add_city(request):

    if request.method == 'GET':
        return render(request, 'templates/gadadmin/add_city.html')

    if request.method == 'POST':

        input_data = request.POST

        if (input_data['name'] or input_data['street'] ):
            city = City.objects.create(
                name=input_data['name'], street=input_data['street'],
                city=input_data['city'], zipcode=input_data['zipcode'],
                area=input_data['area'], partner=input_data['partner'],
                lat=input_data['lat'], lng=input_data['lng'],
            )

            if city:
                messages.success(request, 'New City %s Created '
                                          'successfully.' % input_data['city'])
                return HttpResponseRedirect('/gadadmin/cities_page')
        else:
            messages.error(request, 'Incorrect Username or Password.')
            return render(request, 'templates/gadadmin/add_city.html')


@login_required(login_url='/gadadmin/login')
def remove_city(request, city_id):

    try:
        city = City.objects.get(id=city_id)
        city.delete()
        messages.success(request, 'City removed successfully.')
        return HttpResponseRedirect('/gadadmin/cities_page')
    except City.DoesNotExist:
        messages.warning(request, 'City not found.')
        return HttpResponseRedirect('/gadadmin/cities_page')


@login_required(login_url='/gadadmin/login')
def homepage_content(request, city_name):

    if request.method == 'GET':
        city = City.objects.get(name=city_name)
        cities = City.objects.all()
        homepage_content = HomepageContent.objects.filter(city=city)
        context = {
            "homepage_content": homepage_content,
            "cities": cities,
            "city_name": city_name
        }
        return render(request, 'templates/gadadmin/contents/homepage.html', context)

    if request.method == 'POST':
        input_data = request.POST

        city = City.objects.get(name=city_name)

        HomepageContent.objects.get_or_create(
            city=city,
            name='home_meta_title'
        )
        HomepageContent.objects.get_or_create(
            city=city,
            name='home_meta_description'
        )
        HomepageContent.objects.get_or_create(
            city=city,
            name='home_meta_keywords'
        )
        HomepageContent.objects.get_or_create(
            city=city,
            name='home_meta_schema'
        )

        HomepageContent.objects.get_or_create(city=city, name='home_contact_button')
        HomepageContent.objects.get_or_create(city=city, name='home_section_1')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_2_1')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_2_2')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_2_3')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_2_4')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_3')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_4_1')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_4_2')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_1')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_2')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_3')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_4')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_5')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_6')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_5_7')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_6_1')
        HomepageContent.objects.get_or_create(
            city=city, name='home_section_6_2')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_7_1')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_8_1')

        HomepageContent.objects.get_or_create(
            city=city, name='home_section_9')

        home_contact_button = HomepageContent.objects.get(name='home_contact_button')
        home_contact_button.contents = input_data['home_contact_button']
        home_contact_button.save()

        home_meta_title = HomepageContent.objects.get(name='home_meta_title')
        home_meta_title.contents = input_data['home_meta_title']
        home_meta_title.save()

        home_meta_description = HomepageContent.objects.get(name='home_meta_description')
        home_meta_description.contents = input_data['home_meta_description']
        home_meta_description.save()

        home_meta_keywords = HomepageContent.objects.get(name='home_meta_keywords')
        home_meta_keywords.contents = input_data['home_meta_keywords']
        home_meta_keywords.save()

        home_meta_schema = HomepageContent.objects.get(name='home_meta_schema')
        home_meta_schema.contents = input_data['home_meta_schema']
        home_meta_schema.save()

        home_section_1 = HomepageContent.objects.get(name='home_section_1')
        home_section_1.contents = input_data['home_section_1']
        home_section_1.save()

        home_section_2_1 = HomepageContent.objects.get(name='home_section_2_1')
        home_section_2_1.contents = input_data['home_section_2_1']
        home_section_2_1.save()

        home_section_2_2 = HomepageContent.objects.get(name='home_section_2_2')
        home_section_2_2.contents = input_data['home_section_2_2']
        home_section_2_2.save()

        home_section_2_3 = HomepageContent.objects.get(name='home_section_2_3')
        home_section_2_3.contents = input_data['home_section_2_3']
        home_section_2_3.save()

        home_section_2_4 = HomepageContent.objects.get(name='home_section_2_4')
        home_section_2_4.contents = input_data['home_section_2_4']
        home_section_2_4.save()

        home_section_3 = HomepageContent.objects.get(name='home_section_3')
        home_section_3.contents = input_data['home_section_3']
        home_section_3.save()

        home_section_4_1 = HomepageContent.objects.get(name='home_section_4_1')
        home_section_4_1.contents = input_data['home_section_4_1']
        home_section_4_1.save()

        home_section_4_2 = HomepageContent.objects.get(name='home_section_4_2')
        home_section_4_2.contents = input_data['home_section_4_2']
        home_section_4_2.save()

        home_section_5_1 = HomepageContent.objects.get(name='home_section_5_1')
        home_section_5_1.contents = input_data['home_section_5_1']
        home_section_5_1.save()
        home_section_5_2 = HomepageContent.objects.get(name='home_section_5_2')
        home_section_5_2.contents = input_data['home_section_5_2']
        home_section_5_2.save()
        home_section_5_3 = HomepageContent.objects.get(name='home_section_5_3')
        home_section_5_3.contents = input_data['home_section_5_3']
        home_section_5_3.save()
        home_section_5_4 = HomepageContent.objects.get(name='home_section_5_4')
        home_section_5_4.contents = input_data['home_section_5_4']
        home_section_5_4.save()
        home_section_5_5 = HomepageContent.objects.get(name='home_section_5_5')
        home_section_5_5.contents = input_data['home_section_5_5']
        home_section_5_5.save()
        home_section_5_6 = HomepageContent.objects.get(name='home_section_5_6')
        home_section_5_6.contents = input_data['home_section_5_6']
        home_section_5_6.save()
        home_section_5_7 = HomepageContent.objects.get(name='home_section_5_7')
        home_section_5_7.contents = input_data['home_section_5_7']
        home_section_5_7.save()

        home_section_6_1 = HomepageContent.objects.get(name='home_section_6_1')
        home_section_6_1.contents = input_data['home_section_6_1']
        home_section_6_1.save()
        home_section_6_2 = HomepageContent.objects.get(name='home_section_6_2')
        home_section_6_2.contents = input_data['home_section_6_2']
        home_section_6_2.save()

        home_section_7_1 = HomepageContent.objects.get(name='home_section_7_1')
        home_section_7_1.contents = input_data['home_section_7_1']
        home_section_7_1.save()

        home_section_8_1 = HomepageContent.objects.get(name='home_section_8_1')
        home_section_8_1.contents = input_data['home_section_8_1']
        home_section_8_1.save()

        home_section_9 = HomepageContent.objects.get(name='home_section_9')
        home_section_9.contents = input_data['home_section_9']
        home_section_9.save()

        messages.success(request, 'Content saved successfully.')
        return HttpResponseRedirect('/gadadmin/homepage_content/%s' % city_name)


@login_required(login_url='/gadadmin/login')
def stepone_content(request, city_name):

    if request.method == 'GET':
        city = City.objects.get(name=city_name)
        cities = City.objects.all()
        stepone_content = StepOne.objects.filter(city=city)
        context = {
            "stepone_content": stepone_content,
            "cities": cities,
            "city_name": city_name
        }
        return render(request, 'templates/gadadmin/contents/stepone.html', context)

    if request.method == 'POST':
        input_data = request.POST

        city = City.objects.get(name=city_name)

        StepOne.objects.get_or_create(
            city=city,
            name='stepone_meta_title'
        )
        StepOne.objects.get_or_create(
            city=city,
            name='stepone_meta_description'
        )
        StepOne.objects.get_or_create(
            city=city,
            name='stepone_meta_keywords'
        )
        StepOne.objects.get_or_create(
            city=city,
            name='stepone_meta_schema'
        )

        StepOne.objects.get_or_create(city=city, name='stepone_contact_button')

        StepOne.objects.get_or_create(city=city, name='stepone_section_1')

        StepOne.objects.get_or_create(city=city, name='stepone_section_2_1')
        StepOne.objects.get_or_create(city=city, name='stepone_section_2_2')

        StepOne.objects.get_or_create(city=city, name='stepone_section_3')

        StepOne.objects.get_or_create(city=city, name='stepone_section_4')

        StepOne.objects.get_or_create(city=city, name='stepone_section_5')

        StepOne.objects.get_or_create(city=city, name='stepone_section_6')

        StepOne.objects.get_or_create(city=city, name='stepone_section_7_1')
        StepOne.objects.get_or_create(city=city, name='stepone_section_7_2')
        StepOne.objects.get_or_create(city=city, name='stepone_section_7_3')

        StepOne.objects.get_or_create(city=city, name='stepone_section_8')

        stepone_meta_title = StepOne.objects.get(
            name='stepone_meta_title')
        stepone_meta_title.contents = input_data[
            'stepone_meta_title']
        stepone_meta_title.save()

        stepone_meta_description = StepOne.objects.get(
            name='stepone_meta_description')
        stepone_meta_description.contents = input_data['stepone_meta_description']
        stepone_meta_description.save()

        stepone_meta_keywords = StepOne.objects.get(
            name='stepone_meta_keywords')
        stepone_meta_keywords.contents = input_data[
            'stepone_meta_keywords']
        stepone_meta_keywords.save()

        stepone_meta_schema = StepOne.objects.get(
            name='stepone_meta_schema')
        stepone_meta_schema.contents = input_data[
            'stepone_meta_schema']
        stepone_meta_schema.save()

        stepone_contact_button = StepOne.objects.get(name='stepone_contact_button')
        stepone_contact_button.contents = input_data['stepone_contact_button']
        stepone_contact_button.save()

        stepone_section_1 = StepOne.objects.get(name='stepone_section_1')
        stepone_section_1.contents = input_data['stepone_section_1']
        stepone_section_1.save()

        stepone_section_2_1 = StepOne.objects.get(name='stepone_section_2_1')
        stepone_section_2_1.contents = input_data['stepone_section_2_1']
        stepone_section_2_1.save()
        stepone_section_2_2 = StepOne.objects.get(name='stepone_section_2_2')
        stepone_section_2_2.contents = input_data['stepone_section_2_2']
        stepone_section_2_2.save()

        stepone_section_3 = StepOne.objects.get(name='stepone_section_3')
        stepone_section_3.contents = input_data['stepone_section_3']
        stepone_section_3.save()

        stepone_section_4 = StepOne.objects.get(name='stepone_section_4')
        stepone_section_4.contents = input_data['stepone_section_4']
        stepone_section_4.save()

        stepone_section_5 = StepOne.objects.get(name='stepone_section_5')
        stepone_section_5.contents = input_data['stepone_section_5']
        stepone_section_5.save()

        stepone_section_6 = StepOne.objects.get(name='stepone_section_6')
        stepone_section_6.contents = input_data['stepone_section_6']
        stepone_section_6.save()

        stepone_section_7_1 = StepOne.objects.get(name='stepone_section_7_1')
        stepone_section_7_1.contents = input_data['stepone_section_7_1']
        stepone_section_7_1.save()
        stepone_section_7_2 = StepOne.objects.get(name='stepone_section_7_2')
        stepone_section_7_2.contents = input_data['stepone_section_7_2']
        stepone_section_7_2.save()
        stepone_section_7_3 = StepOne.objects.get(name='stepone_section_7_3')
        stepone_section_7_3.contents = input_data['stepone_section_7_3']
        stepone_section_7_3.save()

        stepone_section_8 = StepOne.objects.get(name='stepone_section_8')
        stepone_section_8.contents = input_data['stepone_section_8']
        stepone_section_8.save()

        messages.success(request, 'Content saved successfully.')
        return HttpResponseRedirect('/gadadmin/stepone_content/%s' % city_name)


@login_required(login_url='/gadadmin/login')
def steptwo_content(request, city_name):

    if request.method == 'GET':
        city = City.objects.get(name=city_name)
        cities = City.objects.all()
        steptwo_content = StepTwo.objects.filter(city=city)
        context = {
            "steptwo_content": steptwo_content,
            "cities": cities,
            "city_name": city_name
        }
        return render(request, 'templates/gadadmin/contents/steptwo.html',
                      context)

    if request.method == 'POST':
        input_data = request.POST

        city = City.objects.get(name=city_name)

        StepTwo.objects.get_or_create(
            city=city, name='steptwo_meta_title')

        StepTwo.objects.get_or_create(
            city=city, name='steptwo_meta_description')

        StepTwo.objects.get_or_create(
            city=city, name='steptwo_meta_keywords')

        StepTwo.objects.get_or_create(
            city=city, name='steptwo_meta_schema')

        StepTwo.objects.get_or_create(city=city, name='steptwo_contact_button')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_1')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_2_1')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_2_2')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_2_3')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_2_4')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_3_1')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_3_2')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_4')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_5_1')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_5_2')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_5_3')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_6_1')
        StepTwo.objects.get_or_create(city=city, name='steptwo_section_6_2')

        StepTwo.objects.get_or_create(city=city, name='steptwo_section_7')

        steptwo_section_1 = StepTwo.objects.get(name='steptwo_section_1')
        steptwo_section_1.contents = input_data['steptwo_section_1']
        steptwo_section_1.save()

        steptwo_contact_button = StepTwo.objects.get(
            name='steptwo_contact_button')
        steptwo_contact_button.contents = input_data[
            'steptwo_contact_button']
        steptwo_contact_button.save()

        steptwo_meta_title = StepTwo.objects.get(
            name='steptwo_meta_title')
        steptwo_meta_title.contents = input_data[
            'steptwo_meta_title']
        steptwo_meta_title.save()

        steptwo_meta_description = StepTwo.objects.get(
            name='steptwo_meta_description')
        steptwo_meta_description.contents = input_data[
            'steptwo_meta_description']
        steptwo_meta_description.save()

        steptwo_meta_keywords = StepTwo.objects.get(
            name='steptwo_meta_keywords')
        steptwo_meta_keywords.contents = input_data[
            'steptwo_meta_keywords']
        steptwo_meta_keywords.save()

        steptwo_meta_schema = StepTwo.objects.get(
            name='steptwo_meta_schema')
        steptwo_meta_schema.contents = input_data[
            'steptwo_meta_schema']
        steptwo_meta_schema.save()

        steptwo_section_2_1 = StepTwo.objects.get(name='steptwo_section_2_1')
        steptwo_section_2_1.contents = input_data['steptwo_section_2_1']
        steptwo_section_2_1.save()
        steptwo_section_2_2 = StepTwo.objects.get(name='steptwo_section_2_2')
        steptwo_section_2_2.contents = input_data['steptwo_section_2_2']
        steptwo_section_2_2.save()
        steptwo_section_2_3 = StepTwo.objects.get(name='steptwo_section_2_3')
        steptwo_section_2_3.contents = input_data['steptwo_section_2_3']
        steptwo_section_2_3.save()
        steptwo_section_2_4 = StepTwo.objects.get(name='steptwo_section_2_4')
        steptwo_section_2_4.contents = input_data['steptwo_section_2_4']
        steptwo_section_2_4.save()

        steptwo_section_3_1 = StepTwo.objects.get(name='steptwo_section_3_1')
        steptwo_section_3_1.contents = input_data['steptwo_section_3_1']
        steptwo_section_3_1.save()
        steptwo_section_3_2 = StepTwo.objects.get(name='steptwo_section_3_2')
        steptwo_section_3_2.contents = input_data['steptwo_section_3_2']
        steptwo_section_3_2.save()

        steptwo_section_4 = StepTwo.objects.get(name='steptwo_section_4')
        steptwo_section_4.contents = input_data['steptwo_section_4']
        steptwo_section_4.save()

        steptwo_section_5_1 = StepTwo.objects.get(name='steptwo_section_5_1')
        steptwo_section_5_1.contents = input_data['steptwo_section_5_1']
        steptwo_section_5_1.save()
        steptwo_section_5_2 = StepTwo.objects.get(name='steptwo_section_5_2')
        steptwo_section_5_2.contents = input_data['steptwo_section_5_2']
        steptwo_section_5_2.save()
        steptwo_section_5_3 = StepTwo.objects.get(name='steptwo_section_5_3')
        steptwo_section_5_3.contents = input_data['steptwo_section_5_3']
        steptwo_section_5_3.save()

        steptwo_section_6_1 = StepTwo.objects.get(name='steptwo_section_6_1')
        steptwo_section_6_1.contents = input_data['steptwo_section_6_1']
        steptwo_section_6_1.save()
        steptwo_section_6_2 = StepTwo.objects.get(name='steptwo_section_6_2')
        steptwo_section_6_2.contents = input_data['steptwo_section_6_2']
        steptwo_section_6_2.save()

        steptwo_section_7 = StepTwo.objects.get(name='steptwo_section_7')
        steptwo_section_7.contents = input_data['steptwo_section_7']
        steptwo_section_7.save()

        messages.success(request, 'Content saved successfully.')
        return HttpResponseRedirect('/gadadmin/steptwo_content/%s' % city_name)


@login_required(login_url='/gadadmin/login')
def stepthree_content(request, city_name):
    if request.method == 'GET':
        city = City.objects.get(name=city_name)
        cities = City.objects.all()
        stepthree_content = StepThree.objects.filter(city=city)
        context = {
            "stepthree_content": stepthree_content,
            "cities": cities,
            "city_name": city_name
        }
        return render(request, 'templates/gadadmin/contents/stepthree.html',
                      context)

    if request.method == 'POST':
        input_data = request.POST

        city = City.objects.get(name=city_name)

        StepThree.objects.get_or_create(
            city=city, name='stepthree_meta_title')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_meta_description')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_meta_keywords')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_meta_schema')

        StepThree.objects.get_or_create(city=city, name='stepthree_contact_button')

        StepThree.objects.get_or_create(city=city, name='stepthree_section_1')

        StepThree.objects.get_or_create(city=city, name='stepthree_section_2')

        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_3_1')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_3_2')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_3_3')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_3_4')

        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_4_1')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_4_2')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_4_3')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_4_4')

        StepThree.objects.get_or_create(city=city, name='stepthree_section_5')

        StepThree.objects.get_or_create(city=city, name='stepthree_section_6')

        stepthree_contact_button = StepThree.objects.get(
            name='stepthree_contact_button')
        stepthree_contact_button.contents = input_data[
            'stepthree_contact_button']
        stepthree_contact_button.save()

        stepthree_meta_title = StepThree.objects.get(
            name='stepthree_meta_title')
        stepthree_meta_title.contents = input_data[
            'stepthree_meta_title']
        stepthree_meta_title.save()

        stepthree_meta_description = StepThree.objects.get(
            name='stepthree_meta_description')
        stepthree_meta_description.contents = input_data[
            'stepthree_meta_description']
        stepthree_meta_description.save()

        stepthree_meta_keywords = StepThree.objects.get(
            name='stepthree_meta_keywords')
        stepthree_meta_keywords.contents = input_data[
            'stepthree_meta_keywords']
        stepthree_meta_keywords.save()

        stepthree_meta_schema = StepThree.objects.get(
            name='stepthree_meta_schema')
        stepthree_meta_schema.contents = input_data[
            'stepthree_meta_schema']
        stepthree_meta_schema.save()

        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_7_1')
        StepThree.objects.get_or_create(
            city=city, name='stepthree_section_7_2')

        stepthree_section_1 = StepThree.objects.get(name='stepthree_section_1')
        stepthree_section_1.contents = input_data['stepthree_section_1']
        stepthree_section_1.save()

        stepthree_section_2 = StepThree.objects.get(name='stepthree_section_2')
        stepthree_section_2.contents = input_data['stepthree_section_2']
        stepthree_section_2.save()

        stepthree_section_3_1 = StepThree.objects.get(name='stepthree_section_3_1')
        stepthree_section_3_1.contents = input_data['stepthree_section_3_1']
        stepthree_section_3_1.save()
        stepthree_section_3_2 = StepThree.objects.get(name='stepthree_section_3_2')
        stepthree_section_3_2.contents = input_data['stepthree_section_3_2']
        stepthree_section_3_2.save()
        stepthree_section_3_3 = StepThree.objects.get(name='stepthree_section_3_3')
        stepthree_section_3_3.contents = input_data['stepthree_section_3_3']
        stepthree_section_3_3.save()
        stepthree_section_3_4 = StepThree.objects.get(name='stepthree_section_3_4')
        stepthree_section_3_4.contents = input_data['stepthree_section_3_4']
        stepthree_section_3_4.save()

        stepthree_section_4_1 = StepThree.objects.get(name='stepthree_section_4_1')
        stepthree_section_4_1.contents = input_data['stepthree_section_4_1']
        stepthree_section_4_1.save()
        stepthree_section_4_2 = StepThree.objects.get(name='stepthree_section_4_2')
        stepthree_section_4_2.contents = input_data['stepthree_section_4_2']
        stepthree_section_4_2.save()
        stepthree_section_4_3 = StepThree.objects.get(name='stepthree_section_4_3')
        stepthree_section_4_3.contents = input_data['stepthree_section_4_3']
        stepthree_section_4_3.save()
        stepthree_section_4_4 = StepThree.objects.get(name='stepthree_section_4_4')
        stepthree_section_4_4.contents = input_data['stepthree_section_4_4']
        stepthree_section_4_4.save()

        stepthree_section_5 = StepThree.objects.get(name='stepthree_section_5')
        stepthree_section_5.contents = input_data['stepthree_section_5']
        stepthree_section_5.save()

        stepthree_section_6 = StepThree.objects.get(name='stepthree_section_6')
        stepthree_section_6.contents = input_data['stepthree_section_6']
        stepthree_section_6.save()

        stepthree_section_7_1 = StepThree.objects.get(name='stepthree_section_7_1')
        stepthree_section_7_1.contents = input_data['stepthree_section_7_1']
        stepthree_section_7_1.save()
        stepthree_section_7_2 = StepThree.objects.get(name='stepthree_section_7_2')
        stepthree_section_7_2.contents = input_data['stepthree_section_7_2']
        stepthree_section_7_2.save()

        messages.success(request, 'Content saved successfully.')
        return HttpResponseRedirect('/gadadmin/stepthree_content/%s' % city_name)
