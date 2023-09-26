from django.contrib import admin

# Register your models here.
from .models import Product, Users,Lesson

admin.site.register(Product)
admin.site.register(Users)
admin.site.register(Lesson)
