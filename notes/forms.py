from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['st_id', 'id_sub', 'id_type_eval',
                  'scolar_year', 'date_note', 'value_note']
        widgets = {
            'st_id': forms.Select(attrs={'class': 'form-control'}),
            'id_sub': forms.Select(attrs={'class': 'form-control'}),
            'id_type_eval': forms.Select(attrs={'class': 'form-control'}),
            'scolar_year': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter school year'}),
            'date_note': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'value_note': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter note value'}),
        }
        labels = {
            'st_id': 'Student',
            'id_sub': 'Subject',
            'id_type_eval': 'Evaluation Type',
            'scolar_year': 'School Year',
            'date_note': 'Date of Note',
            'value_note': 'Note Value',
        }
