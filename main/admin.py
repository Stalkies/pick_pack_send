from django.contrib import admin
from .models import Client, Good, Cart, Photo
# Register your models here.
admin.site.register(Client)
admin.site.register(Good)
admin.site.register(Cart)
admin.site.register(Photo)