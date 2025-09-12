from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Report
from .forms import ReportForm

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            rpt = form.save(commit=False)
            rpt.created_by = request.user
            rpt.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'report_submit.html', {'form': form})

@login_required
def report_list(request):
    reports = Report.objects.order_by('-created_at')
    return render(request, 'report_list.html', {'reports': reports})

@login_required
def report_action(request, report_id, action):
    report = get_object_or_404(Report, id=report_id)

    if action == "accept":
        if report.status != "pending":
            return HttpResponseForbidden("Already handled")
        report.status = "accepted"
        report.accepted_by = request.user
        report.save()
    elif action == "reject":
        if report.status == "pending":
            report.status = "rejected"
            report.accepted_by = request.user
            report.save()
    elif action == "complete":
        if report.accepted_by == request.user:
            if request.method == "POST":
                report.proof = request.FILES.get("proof")
                report.status = "completed"
                report.save()
    return redirect("dashboard")
