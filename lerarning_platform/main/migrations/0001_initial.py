# Generated by Django 4.2.5 on 2023-09-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=50, verbose_name='Имя пользователя')),
                ('videoname', models.TextField(max_length=100, verbose_name='Название видео')),
                ('videolink', models.TextField(max_length=100, verbose_name='Ссылка на видео')),
                ('duration', models.CharField(max_length=100, verbose_name='Продолжительность')),
                ('watch_time', models.CharField(max_length=50, verbose_name='Время просмотра')),
                ('watch_date', models.DateTimeField(max_length=50, verbose_name='Дата  просмотра')),
                ('status', models.TextField(max_length=50, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(max_length=100, verbose_name='Автор')),
                ('name', models.TextField(max_length=100, verbose_name='Название')),
                ('Video', models.CharField(max_length=100, verbose_name='Ссылка')),
                ('duration', models.CharField(max_length=100, verbose_name='Продолжительность')),
                ('about', models.TextField(max_length=300, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True, verbose_name='Имя пльзователя')),
                ('mail', models.TextField(unique=True, verbose_name='Электронная почта')),
                ('password', models.TextField(unique=True, verbose_name='Пароль')),
            ],
        ),
    ]