# COLORAMA URL Configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('colors_app.urls')),
    path('starter_app/', include('starter_app.urls')),
    path('admin/', admin.site.urls),
]
