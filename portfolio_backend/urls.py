"""
    portfolio_backend URL Configuration
    
    The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path

from apps.translatable_content.api.views import (
    PostDetail
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/post/', PostDetail.as_view())
]
