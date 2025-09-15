from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
#router.register(r'friends', FriendInteractionView, basename='allocation')

urlpatterns = [
    #path('allocation', include('controller.urls.py')),
    path('friends', FriendInteractionView.as_view()),
    path('admin/', admin.site.urls),
]