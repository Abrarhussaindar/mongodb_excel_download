# mongodb_excel/urls.py
from django.urls import path
from .views import download_excel

urlpatterns = [
    path('download_excel/', download_excel, name='download_excel'),
]
