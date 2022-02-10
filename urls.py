from django.contrib import admin
from django.urls import path
from app_1.views import qidirish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', qidirish, name='qidirish'),
]