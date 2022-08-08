from django.contrib import admin
from django.urls import path
from main import views


import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index),
]
