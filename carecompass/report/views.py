from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Report
from .forms import ReportForm


@login_required
def submit_report(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        location = request.POST.get("location")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        photo = request.FILES.get("photo")
        video = request.FILES.get("video")

        Report.objects.create(
            title=title,
            description=description,
            location=location,
            latitude=latitude if latitude else None,
            longitude=longitude if longitude else None,
            photo=photo,
            video=video,
            created_by=request.user
        )

        return redirect("report_list")

    return render(request, "report_submit.html")


@login_required
def report_list(request):
    reports = Report.objects.order_by('-created_at')
    return render(request, 'report_list.html', {'reports': reports})


@login_required
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, "report_detail.html", {
        "report": report
    })


@login_required
def report_action(request, report_id, action):
    report = get_object_or_404(Report, id=report_id)

    # Accept
    if action == "accept":
        if report.status == "pending":
            report.status = "accepted"
            report.accepted_by = request.user
            report.save()

    # Reject
    elif action == "reject":
        if report.status == "pending":
            report.status = "rejected"
            report.accepted_by = request.user
            report.save()

    # Complete (with proof) - only for NGO/Volunteer
    elif action == "complete":
        if hasattr(request.user, "role") and request.user.role in ["ngo", "volunteer"]:
            if report.accepted_by == request.user:
                if request.method == "POST" and request.FILES.get("proof"):
                    report.proof = request.FILES["proof"]
                    report.status = "completed"
                    report.save()
        else:
            return HttpResponseForbidden("Only NGO/Volunteer can upload proof.")

    return redirect("report_list")