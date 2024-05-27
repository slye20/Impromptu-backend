# todo/todo/impromptu.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from impromptu_api import urls as impromptu_urls
from .views.list_view import (ImpromptuList)
from .views.detail_view import (ImpromptuDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('impromptu/', include(impromptu_urls)),
    path('api/posts/', ImpromptuList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', ImpromptuDetail.as_view(), name='post-detail')

]