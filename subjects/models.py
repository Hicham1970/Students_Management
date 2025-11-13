from django.db import models

from teachers.models import Teacher


# Create your models here.
class TbTypeSubject(models.Model):
    id_type_sub = models.AutoField(primary_key=True)
    name_type_sub = models.CharField(max_length=150)

    class Meta:
        db_table = 'tb_type_subject'

    def __str__(self):
        return self.name_type_sub


class Subject(models.Model):
    id_sub = models.AutoField(primary_key=True)
    name_sub = models.CharField(max_length=100)
    # Adjust max_digits and decimal_places as needed
    coef_sub = models.DecimalField(max_digits=10, decimal_places=2)
    id_type_sub = models.ForeignKey(TbTypeSubject, on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='subjects')

    class Meta:
        db_table = 'tb_subject'


class TbTypeEvaluation(models.Model):
    id_type_eval = models.AutoField(primary_key=True)
    name_type_eval = models.CharField(max_length=150)

    class Meta:
        db_table = 'tb_type_evaluation'


class Formation(models.Model):
    format_id = models.IntegerField(primary_key=True)
    name_formation = models.CharField(max_length=100)
    # Adjust max_digits and decimal_places as needed
    price_form = models.DecimalField(max_digits=10, decimal_places=2)
    scolar_year = models.CharField(max_length=100, blank=True, null=True)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'formation'
