from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Subject, Formation
from .forms import SubjectForm, FormationForm
from notes.models import Note
from django.db.models import F, ExpressionWrapper, FloatField


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


@login_required
def formation_list(request):
    """Display list of all formations"""
    formations = Formation.objects.select_related('id_teacher').all()
    return render(request, 'subjects/formation.html', {'formations': formations})


@login_required
def formation_create(request):
    """Create a new formation"""
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formation created successfully!')
            return redirect('formations')
    else:
        form = FormationForm()
    return render(request, 'subjects/add-formation.html', {'form': form, 'title': 'Add Formation'})


@login_required
def formation_update(request, pk):
    """Update an existing formation"""
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formation updated successfully!')
            return redirect('formations')
    else:
        form = FormationForm(instance=formation)
    return render(request, 'subjects/edite-formation.html', {'form': form, 'title': 'Edit Formation'})


@login_required
def formation_delete(request, pk):
    """Delete a formation"""
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        formation.delete()
        messages.success(request, 'Formation deleted successfully!')
        return redirect('formations')
    return render(request, 'subjects/formation_confirm_delete.html', {'formation': formation})


@login_required
def formation_notes_comparison(request):
    """Display notes comparison for formations"""
    notes = Note.objects.select_related(
        'st_id__user', 'id_sub', 'id_type_eval').annotate(
        weighted_note=ExpressionWrapper(
            F('value_note') * F('id_sub__coef_sub'),
            output_field=FloatField()
        )
    ).order_by('-date_note')
    return render(request, 'notes/notes-comparaisons.html', {'notes': notes, 'title': 'Notes Comparison for Formations'})
