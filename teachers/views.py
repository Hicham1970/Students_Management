from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from django.contrib import messages
from school.models import Notification
from .forms import TeacherForm
# Create your views here.


def create_notification(user, message):
    Notification.objects.create(user=user, message=message)


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save()
            create_notification(
                request.user, f"Added Teacher: {teacher.first_name} {teacher.last_name}")
            messages.success(
                request, f"Teacher {teacher.first_name} {teacher.last_name} added Successfully")
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, "teachers/add-teacher.html", {'form': form})


def teacher_list(request):
    teacher_list = Teacher.objects.all()
    return render(request, "teachers/teachers.html", {
        'teacher_list': teacher_list
    })


def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            create_notification(
                request.user, f"Edited Teacher: {teacher.first_name} {teacher.last_name}")
            messages.success(
                request, f"Teacher {teacher.first_name} {teacher.last_name} updated Successfully")
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teachers/edit-teacher.html", {'form': form, 'teacher': teacher})


def view_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, "teachers/teacher-details.html", {
        'teacher': teacher
    })


def delete_teacher(request, slug):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
        teacher.delete()
        create_notification(request.user, f"Deleted teacher: {teacher_name}")
        return redirect('teacher_list')

    return HttpResponseForbidden()
