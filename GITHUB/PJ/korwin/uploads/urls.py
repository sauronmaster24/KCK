from django.conf.urls import url
from django.contrib import admin
import random
from uploads.core import views


urlpatterns = [
    url('^$', views.witaj, name='witaj'),
    url('autorzy/', views.autorzy, name='autorzy'),
    url('generator/', views.generator, name='generator'),
]
