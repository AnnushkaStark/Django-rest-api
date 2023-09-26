"""
URL configuration for lerarning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import ProductAPIViev, LessonAPIViev,  UsersAPIViev, ProductStatistic
#router = routers.DefaultRouter()
#router.register('api/lessons',ProductAPIViev)
#router.register('api/lessons_statistic', LessonAPIViev)
#router.register('api/user_statistic', UsersAPIViev)
#router.register('api/productstatistic_statisic', ProductStatistic)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('api/lessons',ProductAPIViev.as_view()),
    path('api/lessons_statistic', LessonAPIViev.as_view()),
    path('api/user_statistic', UsersAPIViev.as_view()),
    path('api/productstatistic_statisic', ProductStatistic.as_view())]
         
