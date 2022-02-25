from django.contrib import admin

# Register your models here.
from users.models import AdvUser, Subscriptions, Social

admin.site.register(AdvUser)
admin.site.register(Subscriptions)
admin.site.register(Social)
