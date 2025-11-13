from django.contrib import admin
from .models import TbTypeSubject, Subject, TbTypeEvaluation, Formation

@admin.register(TbTypeSubject)
class TbTypeSubjectAdmin(admin.ModelAdmin):
    list_display = ('id_type_sub', 'name_type_sub')
    search_fields = ('name_type_sub',)
    ordering = ('name_type_sub',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id_sub', 'name_sub', 'coef_sub', 'id_type_sub', 'id_teacher')
    search_fields = ('name_sub', 'id_type_sub__name_type_sub', 'id_teacher__name')
    list_filter = ('id_type_sub', 'id_teacher')
    ordering = ('name_sub',)

@admin.register(TbTypeEvaluation)
class TbTypeEvaluationAdmin(admin.ModelAdmin):
    list_display = ('id_type_eval', 'name_type_eval')
    search_fields = ('name_type_eval',)
    ordering = ('name_type_eval',)

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('format_id', 'name_formation', 'price_form', 'scolar_year', 'id_teacher')
    search_fields = ('name_formation', 'scolar_year', 'id_teacher__name')
    list_filter = ('scolar_year', 'id_teacher')
    ordering = ('name_formation',)
