from django.urls import path
from colors_app import views
from colors_app.class_based_views import NewColorView, ColorListView

app_name = "colors_app"
urlpatterns = [
    path('', views.home_view, name="index"),
    path('colors/random', views.random_color_view, name="random_color"),
    path('colors/new', NewColorView.as_view(), name='new_color'),
    path('colors', ColorListView.as_view(), name='color_list'),
]

