from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20)
    gender=models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    mobil_number = models.CharField(max_length=15)
    teacher_email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    hired_on= models.DateField()
    teacher_image= models.ImageField(upload_to='teachers/', blank=True)
    is_active=models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(
                f"{self.first_name}-{self.last_name}-{self.teacher_id}")
            self.slug = base_slug
            # Ensure uniqueness
            while Teacher.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{get_random_string(4)}"
        super(Teacher, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"