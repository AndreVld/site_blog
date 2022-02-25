from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class AdvUser(AbstractUser):
    email = models.EmailField(verbose_name='Email адрес', unique=True, error_messages={
        'unique': "A user with that Email already exists."})
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    about_me = models.TextField(verbose_name='Обо мне', max_length=512, blank=True)
    is_confirmed = models.BooleanField(default=True, verbose_name='Подтвердил почту?')
    show_email = models.BooleanField(default=False, verbose_name='Email скрыт?')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
