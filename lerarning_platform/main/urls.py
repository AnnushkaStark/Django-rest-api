from django import views
from django.urls import path
from . import views
from django.http import HttpResponse,JsonResponse
urlpatterns = [
    path('', views.index)
    ]
    