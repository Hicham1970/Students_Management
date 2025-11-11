from django.urls import path
from . import views
from departments.views import add_department

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-admin/', views.dashboard_admin, name='dashboard_admin'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/add-department.html', add_department,
         name='add_department_dashboard'),
    path('notification/mark-as-read/', views.mark_notification_as_read,
         name='mark_notification_as_read'),
    path('notification/clear-all/', views.clear_all_notifications,
         name='clear_all_notifications'),

]
