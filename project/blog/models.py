from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Название статьи')
    content = models.TextField(verbose_name='Содержание статьи')  # Tarifi u togrisidagi malumot
    photo = models.ImageField(upload_to='photos/', verbose_name='Фотография', blank=True,
                              null=True)  # rasm saqlash uchun funksiya
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')  # Yaratilgan paytini saqlab qolishi
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')  # Yangilash payti
    publish = models.BooleanField(default=True, verbose_name='Статус публикации')  # yuklash
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')  # korishlar sonini chiqarish
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория статьи')  # categoriya ozi
    video = models.CharField(max_length=500, verbose_name='Ссылка видео', blank=True, null=True)

    def get_photo(self):  # Ozimizni rasmni qoynaguncha no photo db chiqib turadi
        if self.photo:
            return self.photo.url
        else:
            return "https://us.123rf.com/450wm/alekseyvanin/alekseyvanin1805/alekseyvanin180500364/100739054-no-photo-camera-outline-icon-linear-style-sign-for-mobile-concept-and-web-design-no-photography-simp.jpg?ver=6"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(max_length=500, verbose_name='Категорий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

