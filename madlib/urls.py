from . import views
from django.urls import path

app_name = 'madlib'
urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.madlib_form, name="madlib_form"),
]
