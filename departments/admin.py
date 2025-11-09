from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'dept_code', 'dept_head', 'created_at')  # Supprimé le doublon
    search_fields = ('dept_name', 'dept_code', 'dept_head__first_name', 'dept_head__last_name',
                    'dept_head__teacher_id', 'dept_head__teacher_email')
    list_filter = ('created_at', 'dept_head__subject', 'dept_head__is_active')
    ordering = ('dept_name',)
    raw_id_fields = ('dept_head',)
    
    fieldsets = (
        (None, {
            'fields': ('dept_name', 'dept_code', 'dept_description', 'dept_head', 'dept_location', 'dept_phone', 'dept_email')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
