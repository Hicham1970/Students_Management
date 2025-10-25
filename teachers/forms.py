from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name', 'last_name', 'teacher_id', 'gender',
            'mobil_number', 'teacher_email', 'subject', 'hired_on',
            'teacher_image', 'is_active'
        ]
        widgets = {
            'hired_on': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].initial = True
