from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'id_sub', 'id_type_eval',
                    'scolar_year', 'value_note', 'date_note')
    list_filter = ('scolar_year', 'id_type_eval', 'id_sub')
    search_fields = ('st_id__first_name',
                     'st_id__last_name', 'id_sub__name_sub')
    ordering = ('-date_note',)
