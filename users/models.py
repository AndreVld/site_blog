from django.contrib.auth.models import AbstractUser
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer


# Create your models here.


class AdvUser(AbstractUser):
    email = models.EmailField(verbose_name='Email адрес', unique=True, )
    image = models.ImageField(upload_to='users_images/%Y/%m/%d', blank=True, null=True)
    about_me = models.TextField(verbose_name='About me', max_length=1024, blank=True)
    is_confirmed = models.BooleanField(default=True, verbose_name='Подтвердил почту?')
    show_email = models.BooleanField(default=True, verbose_name='Email скрыт?')


class Subscriptions(models.Model):
    user = models.ForeignKey(AdvUser, related_name='subscribers', on_delete=models.CASCADE)
    sub_on = models.ForeignKey(AdvUser, related_name='sub', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'
        constraints = (models.CheckConstraint(check=~models.Q(sub_on=models.F('user')),
                                              name='users_subscriptions_constrains'),)
        # IntegrityError  не забыть обработать исключение при вызове save()


class Social(models.Model):
    class Names(models.TextChoices):
        VK = 'vkontakte', 'Vkontakte'
        FACEBOOK = 'facebook'
        INSTAGRAM = 'instagram'
        # GITHUB = 'git'
        # YOUTUBE = 'Youtube'
        __empty__ = 'Select the name of the social network'

    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, related_name='social')
    name = models.CharField(max_length=64, choices=Names.choices, verbose_name='Social network')
    link = models.URLField(max_length=512, unique=True)
    image = models.FilePathField(path='static/images/social', blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.image = f'images/social/{self.name}-96.png'
        super(Social, self).save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'social networks'
        verbose_name = 'Social network'
