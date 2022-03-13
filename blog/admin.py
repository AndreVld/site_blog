from django.contrib import admin

# Register your models here.
from blog.models import Tags, Posts, Comments

admin.site.register(Tags)
admin.site.register(Posts)
admin.site.register(Comments)

