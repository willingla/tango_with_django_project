from django.urls import path
from django.urls import re_path
from rango import views
from django.conf.urls import url
app_name = 'rango'

urlpatterns = [
    # re_path(r'^index/$', views.index),
    # re_path(r'^about/$', views.about),
    # path('index/', views.index),
    # path('about/', views.about),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
]
