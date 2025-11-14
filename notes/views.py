from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F, ExpressionWrapper, FloatField
from .models import Note
from .forms import NoteForm
from student.models import Student


@login_required
def note_list(request):
    """Display list of all notes"""
    notes = Note.objects.select_related(
        'st_id', 'id_sub', 'id_type_eval').order_by('-date_note')
    paginator = Paginator(notes, 30)  # Show 30 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes/notes.html', {'page_obj': page_obj})


@login_required
def note_detail(request, id_note):
    """Display details of a specific note"""
    note = get_object_or_404(Note, id_note=id_note)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def note_create(request):
    """Create a new note"""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request, 'notes/add-note.html', {'form': form, 'title': 'Add Note'})


@login_required
def note_update(request, id_note):
    """Update an existing note"""
    note = get_object_or_404(Note, id_note=id_note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit-note.html', {'form': form, 'title': 'Edit Note'})


@login_required
def note_delete(request, id_note):
    """Delete a note"""
    note = get_object_or_404(Note, id_note=id_note)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('notes')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


@login_required
def notes_2021(request):
    """Display notes from the year 2021"""
    notes = Note.objects.filter(scolar_year=2021).select_related(
        'st_id__user', 'id_sub', 'id_type_eval').order_by('-date_note')
    return render(request, 'notes/notes-comparaisons.html', {'notes': notes, 'title': 'Notes for 2021'})


@login_required
def notes_by_student(request, student_id):
    """Display all notes for a specific student"""
    student = get_object_or_404(Student, id=student_id)
    notes = Note.objects.filter(st_id=student).select_related(
        'st_id__user', 'id_sub', 'id_type_eval').order_by('-date_note')
    return render(request, 'notes/notes-comparaisons.html', {'notes': notes, 'student': student, 'title': f'Notes for {student}'})


@login_required
def notes_comparison(request):
    """Display notes comparison for all notes"""
    notes = Note.objects.select_related(
        'st_id__user', 'id_sub', 'id_type_eval').annotate(
        weighted_note=ExpressionWrapper(
            F('value_note') * F('id_sub__coef_sub'),
            output_field=FloatField()
        )
    ).order_by('-date_note')
    return render(request, 'notes/notes-comparaisons.html', {'notes': notes, 'title': 'Notes Comparison'})
