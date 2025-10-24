from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import CustomUser
from .forms import CustomUserChangeForm
from report.models import Report


@login_required
def dashboard(request):
    if request.user.role == "user":
        report_count = Report.objects.filter(created_by=request.user).count()
        return render(request, "dashboard_user.html", {"count": report_count})

    elif request.user.role == "volunteer":
        # Accepted reports by this volunteer
        accepted_reports = Report.objects.filter(
            accepted_by=request.user,
            status='accepted'
        )

        # Completed reports by this volunteer
        completed_reports = Report.objects.filter(
            accepted_by=request.user,
            status='completed'
        )

        # All reports for the volunteer (accepted + completed)
        my_reports = Report.objects.filter(
            accepted_by=request.user,
            status__in=['accepted', 'completed']
        )

        return render(request, "dashboard_volunteer.html", {
            "accepted_reports": accepted_reports,
            "completed_reports": completed_reports,
            "my_reports": my_reports
        })

    elif request.user.role == "ngo":
        # Accepted reports by this NGO
        accepted_reports = Report.objects.filter(
            accepted_by=request.user,
            status='accepted'
        )

        # Completed reports by this NGO
        completed_reports = Report.objects.filter(
            accepted_by=request.user,
            status='completed'
        )

        # All reports for the NGO (accepted + completed)
        my_reports = Report.objects.filter(
            accepted_by=request.user,
            status__in=['accepted', 'completed']
        )

        return render(request, "dashboard_ngo.html", {
            "accepted_reports": accepted_reports,
            "completed_reports": completed_reports,
            "my_reports": my_reports
        })

    return redirect("home")


@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserChangeForm(instance=user)

    skills_list = []
    if user.skills:
        skills_list = [s.strip() for s in user.skills.split(',') if s.strip()]

    return render(request, "profile.html", {
        "user": user,
        "form": form,
        "skills_list": skills_list
    })
