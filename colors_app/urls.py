from django.urls import path
from colors_app import views

app_name = "colors_app"
urlpatterns = [
    path('', views.home_view, name="index"),
    path('colors/random', views.random_color_view, name="random_color"),
]

