# todo/todo/impromptu.py : Main urls.py
from django.contrib import admin
from django.urls import path
from .views.list_view import (ImpromptuList)
from .views.detail_view import (ImpromptuDetail)
from .views.auth_view import login, signup

urlpatterns = [
    path('posts/', ImpromptuList.as_view(), name='post-list'),
    path('posts/<int:pk>/', ImpromptuDetail.as_view(), name='post-detail'),
    path('login/', login),
    path('signup/', signup),
]