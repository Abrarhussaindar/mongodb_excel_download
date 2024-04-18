# mongodb_excel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('download_skillgap_excel/', views.download_skillgap_excel, name='download_skillgap_excel'),
    path('download_youthaspiration_excel/', views.download_youthaspiration_excel, name='download_youthaspiration_excel'),
]
