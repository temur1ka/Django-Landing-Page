
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rusiko/', admin.site.urls),
    path('', include('charts.urls')),
]
