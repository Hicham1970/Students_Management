from django.urls import path
from .views import *

urlpatterns = [
    path('notes/', note_list, name='notes'),  # Liste des notes
    path('note/create/', note_create, name='note_create'),  # Création d'une note
    path('note/<int:id_note>/', note_detail,
         name='note_detail'),  # Détails d'une note
    path('note/<int:id_note>/update/', note_update,
         name='note_update'),  # Mise à jour d'une note
    path('note/<int:id_note>/delete/', note_delete,
         name='note_delete'),  # Suppression d'une note
    path('notes/2021/', notes_2021, name='notes_2021'),  # Notes for 2021
    path('notes/student/<int:student_id>/', notes_by_student,
         name='notes_by_student'),  # Notes by student
    path('notes/notes_comparaison.html', notes_comparison,
         name='notes_comparison'),  # Notes comparison
]
