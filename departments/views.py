from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from teachers.models import Teacher  # Ajout pour récupérer Teacher
from django.contrib import messages
from school.models import Notification  # Assumer que c'est correct

def create_notification(user, message):
    Notification.objects.create(user=user, message=message)

def add_department(request):
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        dept_code = request.POST.get('dept_code')
        dept_description = request.POST.get('dept_description')
        dept_head_id = request.POST.get('dept_head')  # Récupérer l'ID
        dept_location = request.POST.get('dept_location')
        dept_phone = request.POST.get('dept_phone')
        dept_email = request.POST.get('dept_email')

        # Validation basique
        if not dept_name:
            messages.error(request, "Le nom du département est requis.")
            return redirect("add_department")

        # Récupérer l'objet Teacher si fourni
        dept_head = None
        if dept_head_id:
            try:
                dept_head = get_object_or_404(Teacher, id=dept_head_id)
            except:
                messages.error(request, "Chef de département invalide.")
                return redirect("add_department")

        # Créer le département
        department = Department.objects.create(
            dept_name=dept_name,
            dept_code=dept_code,
            dept_description=dept_description,
            dept_head=dept_head,
            dept_location=dept_location,
            dept_phone=dept_phone,
            dept_email=dept_email
        )

        create_notification(request.user, f"Added Department: {department.dept_name}")
        messages.success(request, f"Department {department.dept_name} added Successfully")
        return redirect("department_list")

    # Pour GET, passer la liste des teachers pour le formulaire
    teachers = Teacher.objects.filter(is_active=True)  # Seulement les actifs
    return render(request, "departments/add-department.html", {'teachers': teachers})  # Template corrigé

def department_list(request):
    departments = Department.objects.all()  # Corrigé
    context = {
        'department_list': departments,  # Corrigé
    }
    return render(request, "departments/departments.html", context)

def edit_department(request, slug):  # Renommé
    department = get_object_or_404(Department, slug=slug)
    
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        dept_code = request.POST.get('dept_code')
        dept_description = request.POST.get('dept_description')
        dept_head_id = request.POST.get('dept_head')
        dept_location = request.POST.get('dept_location')
        dept_phone = request.POST.get('dept_phone')
        dept_email = request.POST.get('dept_email')

        # Validation
        if not dept_name:
            messages.error(request, "Le nom du département est requis.")
            return redirect("edit_department", slug=slug)

        # Récupérer Teacher
        dept_head = None
        if dept_head_id:
            try:
                dept_head = get_object_or_404(Teacher, id=dept_head_id)
            except:
                messages.error(request, "Chef de département invalide.")
                return redirect("edit_department", slug=slug)

        # Mettre à jour
        department.dept_name = dept_name
        department.dept_code = dept_code
        department.dept_description = dept_description
        department.dept_head = dept_head
        department.dept_location = dept_location
        department.dept_phone = dept_phone
        department.dept_email = dept_email
        department.save()
        
        create_notification(request.user, f"Edited Department: {department.dept_name}")
        messages.success(request, f"Department {department.dept_name} updated successfully")
        return redirect("department_list")

    # Pour GET, passer les données et la liste des teachers
    teachers = Teacher.objects.filter(is_active=True)
    return render(request, "departments/edit-department.html", {
        'department': department,  # Passer l'objet entier pour simplicité
        'teachers': teachers,
    })

def view_department(request, slug):
    department = get_object_or_404(Department, slug=slug)
    context = {
        'department': department
    }
    return render(request, "departments/department-details.html", context)

def delete_department(request, slug):
    if request.method == "POST":
        department = get_object_or_404(Department, slug=slug)
        dept_name = department.dept_name
        department.delete()
        create_notification(request.user, f"Deleted Department: {dept_name}")
        messages.success(request, f"Department {dept_name} deleted successfully")
        return redirect('department_list')
    return HttpResponseForbidden()