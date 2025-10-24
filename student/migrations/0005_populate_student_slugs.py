# e:\Dev\python_files\Django\School\Home\student\migrations\XXXX_populate_student_slugs.py

from django.db import migrations
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Student = apps.get_model('student', 'Student')
    for student in Student.objects.all():
        if not student.slug:
            # Manually create a slug if one doesn't exist.
            # This logic should ideally match your pre_save signal.
            base_slug = slugify(
                f"{student.first_name}-{student.last_name}-{student.student_id}")
            student.slug = base_slug
            student.save()


class Migration(migrations.Migration):

    dependencies = [
        # Make sure this matches your previous migration
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
