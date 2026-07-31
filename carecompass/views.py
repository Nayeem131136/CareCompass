from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from report.models import Report


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password. Please try again.'
    return render(request, 'registration/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to CareCompass, {user.username}!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    if user.role == 'user':
        my_reports = Report.objects.filter(created_by=user).order_by('-created_at')
        return render(request, 'dashboard_user.html', {
            'reports':   my_reports,
            'count':     my_reports.count(),
            'pending':   my_reports.filter(status='pending').count(),
            'accepted':  my_reports.filter(status='accepted').count(),
            'completed': my_reports.filter(status='completed').count(),
            'rejected':  my_reports.filter(status='rejected').count(),
        })
    elif user.role == 'volunteer':
        return render(request, 'dashboard_volunteer.html', {
            'accepted_reports':  Report.objects.filter(accepted_by=user, status='accepted').order_by('-created_at'),
            'completed_reports': Report.objects.filter(accepted_by=user, status='completed').order_by('-created_at'),
            'pending_reports':   Report.objects.filter(status='pending').order_by('-created_at'),
        })
    elif user.role == 'ngo':
        return render(request, 'dashboard_ngo.html', {
            'accepted_reports':  Report.objects.filter(accepted_by=user, status='accepted').order_by('-created_at'),
            'completed_reports': Report.objects.filter(accepted_by=user, status='completed').order_by('-created_at'),
            'pending_reports':   Report.objects.filter(status='pending').order_by('-created_at'),
        })
    return redirect('home')


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        user.phone             = request.POST.get('phone', user.phone or '')
        user.address           = request.POST.get('address', user.address or '')
        user.bio               = request.POST.get('bio', user.bio or '')
        user.organization_name = request.POST.get('organization_name', user.organization_name or '')
        user.skills            = request.POST.get('skills', user.skills or '')
        if 'profile_pic'  in request.FILES: user.profile_pic  = request.FILES['profile_pic']
        if 'certificate'  in request.FILES: user.certificate  = request.FILES['certificate']
        if 'license_file' in request.FILES: user.license_file = request.FILES['license_file']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    # Stats for profile page
    if user.role == 'user':
        stats = {
            'total':     Report.objects.filter(created_by=user).count(),
            'completed': Report.objects.filter(created_by=user, status='completed').count(),
            'pending':   Report.objects.filter(created_by=user, status='pending').count(),
        }
    else:
        stats = {
            'total':     Report.objects.filter(accepted_by=user).count(),
            'completed': Report.objects.filter(accepted_by=user, status='completed').count(),
            'active':    Report.objects.filter(accepted_by=user, status='accepted').count(),
        }

    skills_list = [s.strip() for s in (user.skills or '').split(',') if s.strip()]
    return render(request, 'profile.html', {
        'user': user,
        'skills_list': skills_list,
        'stats': stats,
    })
