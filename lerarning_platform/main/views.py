from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum, Count, Case, When, FloatField
from .models import Product, Users, Lesson
from rest_framework import generics
from .serializers import ProductSerializer ,UsersSerializer, LessonSerializer, ProductStatisticSerializer


class ProductAPIViev(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
   
    

class UsersAPIViev(generics.ListAPIView):
    queryset  = Users.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['get']
    

class LessonAPIViev(generics.ListAPIView):
    queryset  = Lesson.objects.all()
    serializer_class = LessonSerializer
    http_method_names = ['get']
    

    

class ProductStatistic(generics.ListAPIView): 
    serializer_class = ProductStatisticSerializer
    def get_queryset(self):
        total_lessons = str(Lesson.objects.count())
        total_users =str(Users.objects.count())
        total_viewing_time = str(Lesson.objects.aggregate(total_viewing_time=Sum('watch_time'))['total_viewing_time'])
        prod_stat = str(int(total_lessons) / int(total_users) * 100)
      
        return   total_lessons, total_users ,total_viewing_time, prod_stat

    
    http_method_names = ['get']
        
def index(request):
    return HttpResponse('<h1>Привет Мир!</h1>')


