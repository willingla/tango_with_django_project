from django.urls import path
from django.urls import re_path
from rango import views

app_name = 'rango'

urlpatterns = [
    # re_path(r'^index/$', views.index),
    # re_path(r'^about/$', views.about),
    # path('index/', views.index),
    # path('about/', views.about),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
