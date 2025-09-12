from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from report.models import Report

@login_required
def dashboard(request):
    if request.user.role == "user":
        report_count = Report.objects.filter(created_by=request.user).count()
        return render(request, "dashboard_user.html", {"count": report_count})
    elif request.user.role == "volunteer":
        reports = Report.objects.filter(status="pending")
        return render(request, "dashboard_volunteer.html", {"reports": reports})
    elif request.user.role == "ngo":
        reports = Report.objects.filter(status="pending")
        return render(request, "dashboard_ngo.html", {"reports": reports})
    return redirect("home")

@login_required
def profile(request):
    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.phone = request.POST.get("phone")
        request.user.bio = request.POST.get("bio")
        if request.FILES.get("profile_pic"):
            request.user.profile_pic = request.FILES["profile_pic"]
        request.user.save()
        return redirect("profile")
    return render(request, "profile.html", {"user": request.user})
