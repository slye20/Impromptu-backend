# todo/todo/impromptu.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from impromptu_api import urls as impromptu_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('impromptu/', include(impromptu_urls)),
]