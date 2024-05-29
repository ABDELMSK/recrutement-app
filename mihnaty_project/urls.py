
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jobs.urls')),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('users.urls')),
]