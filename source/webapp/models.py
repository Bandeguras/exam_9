from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = [('on moderate', 'На модерацию'), ('published', 'Опубликовано'), ('rejected', 'Отклонено'), ('For removal', 'На удаление')]

# Create your models here.


class Ad(models.Model):
    avatar = models.ImageField(blank=True, null=True, upload_to='user_avatar', verbose_name="Аватар")
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, verbose_name="Описание", null=True, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='ads',
                               verbose_name="Автор")
    category = models.ForeignKey('webapp.Category', on_delete=models.PROTECT, related_name='categories')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновление")
    published_at = models.DateTimeField(verbose_name="Дата публикации")

    def get_absolute_url(self):
        return reverse('webapp:ad', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Статус")

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    ad = models.ForeignKey('webapp.Ad', on_delete=models.CASCADE, related_name='comments',
                                verbose_name="объявление")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='comments',
                               verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'