from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from teachers.models import Teacher

class Department(models.Model):
    # Champs de base
    dept_name = models.CharField(max_length=100, unique=True, verbose_name="Nom du département")
    dept_code = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name="Code du département (ex: Dept01)")
    dept_description = models.TextField(blank=True, verbose_name="Description")
    
    # Chef de département (relation avec Teacher)
    dept_head = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='department_head', verbose_name="Chef de département")
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour le")
    
    # Champs optionnels pour extension
    dept_location = models.CharField(max_length=200, blank=True, verbose_name="Emplacement (bâtiment, salle)")
    dept_phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    dept_email = models.EmailField(blank=True, verbose_name="Email de contact")
    
    # Slug pour les URLs
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")
    
    # Relations potentielles (commentées car les apps n'existent pas encore)
    # courses = models.ManyToManyField('courses.Course', blank=True, related_name='departments', verbose_name="Cours associés")
    # students = models.ManyToManyField('students.Student', blank=True, related_name='departments', verbose_name="Étudiants inscrits")
    
    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
        ordering = ['dept_name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.dept_name}-{self.dept_code}")
            self.slug = base_slug
            while Department.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{get_random_string(4)}"
        super(Department, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.dept_code} - {self.dept_name}" if self.dept_code else self.dept_name
