from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('cms/', include('cms.urls')),
    path('main/', include('main.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
