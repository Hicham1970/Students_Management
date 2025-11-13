from django import forms
from .models import Subject, Formation


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


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['format_id', 'name_formation',
                  'price_form', 'scolar_year', 'id_teacher']
        widgets = {
            'format_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter formation ID'}),
            'name_formation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter formation name'}),
            'price_form': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter price'}),
            'scolar_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school year'}),
            'id_teacher': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'format_id': 'Formation ID',
            'name_formation': 'Formation Name',
            'price_form': 'Price',
            'scolar_year': 'School Year',
            'id_teacher': 'Teacher',
        }
