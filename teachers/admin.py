from django.contrib import admin
from .models import Teacher
from school.models import Notification


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'teacher_id', 'gender',
                    'mobil_number', 'teacher_email', 'subject', 'hired_on', 'is_active')
    search_fields = ('first_name', 'last_name', 'teacher_id',
                     'teacher_email', 'subject')
    list_filter = ('gender', 'is_active')
    # Optional: makes the image field read-only
    readonly_fields = ('teacher_image',)

    def save_model(self, request, obj, form, change):
        """
        Surchargé pour créer une notification lors de l'ajout ou de la modification d'un enseignant.
        """
        super().save_model(request, obj, form, change)
        message = f"Added Teacher: {obj.first_name} {obj.last_name}" if not change else f"Edited Teacher: {obj.first_name} {obj.last_name}"
        Notification.objects.create(user=request.user, message=message)
