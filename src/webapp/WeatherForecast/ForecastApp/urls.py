from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/visual', views.visual, name='visual')
]