from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import create_feed

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    #path('allocation', include('controller.urls.py')),
    path('feed/<int:user_id>', create_feed)
]
