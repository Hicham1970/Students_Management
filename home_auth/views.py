from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, PasswordResetRequest
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_protect


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # Get role from the form (student, teacher, or admin)
        # role = request.POST.get('role')

        # Create the user
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        # Assign the appropriate role
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True

        user.save()  # Save the user with the assigned role
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('index')  # Redirect to the index or home page
    # Render signup template
    return render(request, 'authentification/register.html')


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')

            # Redirect user based on their role
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid user role')
                return redirect('index')  # Redirect to index in case of error

        else:
            messages.error(request, 'Invalid credentials')
    # Render login template
    return render(request, 'authentification/login.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.filter(email=email).first()

        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(
                user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, 'Reset link sent to your email.')
        else:
            messages.error(request, 'Email not found.')

    # Render forgot password template
    return render(request, 'authentification/forgot-password.html')


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()

    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Invalid or expired reset link')
        return redirect('index')

    if request.method == 'POST':
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'Password reset successful')
        return redirect('login')

    # Render reset password template
    return render(request, 'authentification/reset-password.html', {'token': token})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
