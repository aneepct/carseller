from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_session_city', views.update_session_city, name='update_session_city'),
    path('step_one', views.step_one, name='step_one'),
    path('step_two', views.step_two, name='step_two'),
    path('step_three', views.step_three, name='step_three'),
    path('city_page', views.city_page, name='city_page'),
    path('submit_request', views.submit_request, name='submit_request'),
    path('get_car_models/<int:car_brand_id>', views.get_car_models, name='get_car_models'),
    path('get_car_years/<int:car_model_id>', views.get_car_years, name='get_car_years'),
    path('update_location_city/<int:city_id>', views.update_location_city, name='update_location_city'),
    path('.well-known/pki-validation/2F3200EA6A9E9606DC07BFCC343C8D13.txt', views.read_file),
]
