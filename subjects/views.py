from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Subject
from .forms import SubjectForm


@login_required
def subject_list(request):
    """Display list of all subjects"""
    subjects = Subject.objects.select_related(
        'id_type_sub', 'id_teacher').all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})


@login_required
def subject_detail(request, pk):
    """Display details of a specific subject"""
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subjects/subject_detail.html', {'subject': subject})


@login_required
def subject_create(request):
    """Create a new subject"""
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject created successfully!')
            return redirect('subjects')
    else:
        form = SubjectForm()
    return render(request, 'subjects/add-subject.html', {'form': form, 'title': 'Add Subject'})


@login_required
def subject_update(request, pk):
    """Update an existing subject"""
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject updated successfully!')
            return redirect('subjects')
    else:
        form = SubjectForm(instance=subject)
    from .models import TbTypeSubject
    from teachers.models import Teacher
    subject_types = TbTypeSubject.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'subjects/edite-subject.html', {'subject': subject, 'subject_types': subject_types, 'teachers': teachers})


@login_required
def subject_delete(request, pk):
    """Delete a subject"""
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, 'Subject deleted successfully!')
        return redirect('subjects')
    return render(request, 'subjects/subject_confirm_delete.html', {'subject': subject})
