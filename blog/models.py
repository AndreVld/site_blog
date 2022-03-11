from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

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
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    sub_headline = models.CharField(max_length=200, null=True, blank=True, verbose_name='Подзаголовок')
    body = RichTextUploadingField(null=True, blank=True, verbose_name='Пост')
    tags = models.ManyToManyField(Tags, blank=True, null=True)
    featured = models.BooleanField(default=False, verbose_name='Опубликовать сразу?')
    active = models.BooleanField(default=False, verbose_name='Активен?')
    likes = models.IntegerField(default=0, blank=True, verbose_name='Количество просмотров')
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.slug is None:
            slug = slugify(self.headline)

            has_slug = Posts.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                slug = f'{slugify(self.headline)}-{count}'
                has_slug = Posts.objects.filter(slug=slug).exists()
                count += 1
            self.slug = slug

        super(Posts, self).save()

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super(Posts, self).delete()

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):
    pass
