from rest_framework import serializers
from .models import Product, Lesson, Users
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProductStatisticSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        model = Users
        model = Lesson


        fields = '__all__'
        



