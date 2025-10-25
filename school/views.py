from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification

# Create your views here.


def index(request):
    return render(request, 'authentification/login.html')


def dashboard(request):
    return render(request, 'students/student-dashboard.html')


# add more views for Notification

def mark_notification_as_read(request):
    # Logic to mark the notification as read
    if request.method == 'POST':
        notification = Notification.objects.filter(
            user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()


def clear_all_notifications(request):
    # Logic to clear all notifications
    if request.method == 'POST':
        Notification.objects.filter(user=request.user).delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()
