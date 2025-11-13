from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name_sub', 'coef_sub', 'id_type_sub', 'id_teacher']
        widgets = {
            'name_sub': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject name'}),
            'coef_sub': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter coefficient'}),
            'id_type_sub': forms.Select(attrs={'class': 'form-control'}),
            'id_teacher': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name_sub': 'Subject Name',
            'coef_sub': 'Coefficient',
            'id_type_sub': 'Subject Type',
            'id_teacher': 'Teacher',
        }
