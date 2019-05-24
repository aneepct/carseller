from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path(r'', views.index, name='index'),
    path(r'login', views.login_view, name='login_view'),
    path(r'logout/', views.logout_view, name='logout_view'),
    path(r'dashboard', views.dashboard, name='dashboard'),
    path(r'cities_page', views.cities_page, name='cities_page'),
    path(r'add_city', views.add_city, name='add_city'),
    path(r'remove_city/<int:city_id>', views.remove_city, name='remove_city'),
    path(r'homepage_content/<slug:city_name>', views.homepage_content,
         name='homepage_content'),
    path(r'stepone_content/<slug:city_name>', views.stepone_content,
         name='stepone_content'),
    path(r'steptwo_content/<slug:city_name>', views.steptwo_content,
         name='steptwo_content'),
    path(r'stepthree_content/<slug:city_name>', views.stepthree_content,
         name='stepthree_content'),
]
