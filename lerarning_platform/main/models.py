from django.db import models
class Product(models.Model):
    author = models.TextField('Автор', max_length=100,null= False)
    name = models.TextField('Название',max_length=100,null= False)
    Video = models.CharField('Ссылка',max_length=100,null= False)
    duration = models.CharField('Продолжительность',max_length=100,null= False)
    about = models.TextField('Описание',max_length=300,null= False)
    def __str__(self):
        return self.title

    

class Users(models.Model):
    username = models.TextField('Имя пользователя', null= False, unique= True)
    mail = models.TextField('Электронная почта', null= False, unique= True)
    password = models.TextField('Пароль', null= False, unique= True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    username = models.TextField('Имя пользователя',max_length= 50,null= False)
    videoname = models.TextField('Название видео',max_length= 100,null= False)
    videolink = models.TextField('Ссылка на видео',max_length= 100,null= False)
    duration = models.CharField('Продолжительность',max_length=100,null= False)
    watch_time =  models.CharField('Время просмотра',max_length=50,null= False)
    watch_date =  models.DateTimeField('Дата  просмотра',max_length=50,null= False)
    status =  models.TextField('Статус',max_length=50,null= False)

    def __str__(self):
        return self.title    


