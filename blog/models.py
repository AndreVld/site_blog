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
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Posts(models.Model):
    author = models.ForeignKey(AdvUser, related_name='posts', on_delete=models.CASCADE, verbose_name='Автор поста')
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    sub_headline = models.CharField(max_length=200, null=True, blank=True, verbose_name='Подзаголовок')
    body = RichTextUploadingField(null=True, blank=True, verbose_name='Пост')
    tags = models.ManyToManyField(Tags, blank=True)
    featured = models.BooleanField(default=False, verbose_name='Опубликовать сразу?')
    active = models.BooleanField(default=False, verbose_name='Активен?')
    likes = models.IntegerField(default=0, blank=True, verbose_name='Количество просмотров')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, null=True, related_name='comments_for_post')
    comment_author = models.ForeignKey(AdvUser, on_delete=models.SET('deleted user'),related_name='comments_by_author')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True,
                                       related_name='comments_for_parent')
    comment = models.TextField(default='', max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.comment_author} | {self.comment[:20]}...'
