from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('add/', views.add_department, name='add_department'),
    path('edit/<slug:slug>/', views.edit_department, name='edit_department'),
    path('view/<slug:slug>/', views.view_department, name='view_department'),
    path('delete/<slug:slug>/', views.delete_department, name='delete_department'),
    path('dashboard/', views.department_dashboard, name='department_dashboard'),
]
