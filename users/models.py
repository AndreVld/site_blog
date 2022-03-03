from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class AdvUser(AbstractUser):
    email = models.EmailField(verbose_name='Email адрес', unique=True, error_messages={
        'unique': "A user with that Email already exists."})
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    about_me = models.TextField(verbose_name='Обо мне', max_length=512, blank=True)
    is_confirmed = models.BooleanField(default=True, verbose_name='Подтвердил почту?')
    show_email = models.BooleanField(default=True, verbose_name='Email скрыт?')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Subscriptions(models.Model):
    user = models.ForeignKey(AdvUser, related_name='subscribers', on_delete=models.CASCADE)
    sub_on = models.ForeignKey(AdvUser, related_name='sub', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'
        constraints = (models.CheckConstraint(check=models.Q(sub_on=models.F('user')),
                                              name='users_subscriptions_constrains'),)
        # IntegrityError  не забыть обработать исключение при вызове save()


class Social(models.Model):
    class Names(models.TextChoices):
        VK = 'vkontakte-96.png', 'Вконтакте'
        FACEBOOK = 'facebook-96.png'
        INSTAGRAM = 'instagram-96.png'
        # GITHUB = 'git'
        # YOUTUBE = 'Youtube'

        __empty__ = 'Select the name of the social network'

    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, related_name='social')
    name = models.CharField(max_length=64, choices=Names.choices, verbose_name='Social network')
    link = models.URLField(max_length=512, unique=True)
    image = models.FilePathField(path='static/images/social')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Соц. сети'
        verbose_name = 'Соц. сеть'
