# plant_app/urls.py
from django.urls import path

from . import views

app_name = 'app_plante_detect'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('classify/', views.classify, name='classify'),
    path('historique/', views.historique_predictions, name='history'),
]