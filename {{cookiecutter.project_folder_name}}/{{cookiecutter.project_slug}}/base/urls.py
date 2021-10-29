from django.urls import path

from {{cookiecutter.project_slug}}.base import views


app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
]
