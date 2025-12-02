from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("spa_tables/", include("spa_tables.urls", namespace="spa_tables")),
]
