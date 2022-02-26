from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
from users.models import AdvUser


class Tags(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тег')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Posts(models.Model):
    author = models.ForeignKey(AdvUser, related_name='posts', on_delete=models.CASCADE, verbose_name='Автор поста')
    tags = models.ManyToManyField(Tags, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    sub_headline = models.CharField(max_length=200, null=True, blank=True, verbose_name='Подзаголовок')
    body = RichTextField(null=True, blank=True, verbose_name='Текст поста')
    featured = models.BooleanField(default=False, verbose_name='Опубликован?')
    active = models.BooleanField(default=False, verbose_name='Активен?')
    likes = models.IntegerField(default=0, blank=True, verbose_name='Количество просмотров')
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.slug is None:
            slug = slugify(self.headline, allow_unicode=True)

            has_slug = Posts.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug += f'{slugify(self.headline, allow_unicode=True)}-{count}'
                has_slug = Posts.objects.filter(slug=slug).exists()
            self.slug = slug

        super(Posts, self).save()

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):
    pass
