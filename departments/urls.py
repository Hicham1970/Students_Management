from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name='department_list'),
    path("add/", views.add_student, name="add_department"),
    path('departments/<str:slug>/', views.view_student, name='view_department'),
    path('edit/<str:slug>/', views.edit_student, name='edit_department'),
    path('delete/<str:slug>/', views.delete_student, name='delete_department'),



]
