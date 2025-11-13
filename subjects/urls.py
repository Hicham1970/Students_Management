from django.urls import path
from .views import *

urlpatterns = [
    path('subjects/', subject_list, name='subjects'),  # Liste des sujets
    path('subject/<int:pk>/', subject_detail,
         name='subject_detail'),  # Détails d'un sujet
    path('subject/create/', subject_create,
         name='subject_create'),  # Création d'un sujet
    path('subject/<int:pk>/update/', subject_update,
         name='subject_update'),  # Mise à jour d'un sujet
    path('subject/<int:pk>/delete/', subject_delete,
         name='subject_delete'),  # Suppression d'un sujet
]
