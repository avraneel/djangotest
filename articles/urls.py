from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug:slug>', views.article_detail)
]