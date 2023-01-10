from django.contrib import admin
from django.urls import path
from .views import home, delete, itemSave, update

urlpatterns = [
    path('', home, name='home'),
    path('', itemSave, name='itemSave'),
    path('delete/<id>/', delete, name='delete'),
    path('update/<id>/', update, name='update'),
]
