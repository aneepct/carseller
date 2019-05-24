from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_car_data', views.upload_car_data, name='upload_car_data'),
]
