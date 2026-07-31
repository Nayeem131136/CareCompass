from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Report


@login_required
def submit_report(request):
    if request.method == 'POST':
        title       = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        location    = request.POST.get('location', '')
        latitude    = request.POST.get('latitude') or None
        longitude   = request.POST.get('longitude') or None
        photo = request.FILES.get('photo')
        video = request.FILES.get('video')

        if not title or not description:
            return render(request, 'report_submit.html',
                          {'error': 'Title and description are required.'})

        Report.objects.create(
            title=title, description=description,
            location=location,
            latitude=float(latitude)  if latitude  else None,
            longitude=float(longitude) if longitude else None,
            photo=photo, video=video,
            created_by=request.user,
        )
        from django.contrib import messages
        from django.contrib import messages as msg
        msg.success(request, 'Your report has been submitted successfully!')
        return redirect('dashboard')

    return render(request, 'report_submit.html')


@login_required
def report_list(request):
    user = request.user
    # User sees only their own reports; NGO/Volunteer see all
    if user.role == 'user':
        reports = Report.objects.filter(created_by=user).order_by('-created_at')
    else:
        reports = Report.objects.order_by('-created_at')

    status_filter = request.GET.get('status', '')
    if status_filter:
        reports = reports.filter(status=status_filter)

    return render(request, 'report_list.html', {
        'reports': reports,
        'status_filter': status_filter,
    })


@login_required
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'report_detail.html', {'report': report})


@login_required
def report_action(request, report_id, action):
    report = get_object_or_404(Report, id=report_id)
    user   = request.user
    role   = getattr(user, 'role', '')

    if action == 'accept':
        can_accept = (
            report.status == 'pending' or
            (report.status == 'rejected' and report.accepted_by != user)
        )
        if can_accept and role in ['ngo', 'volunteer']:
            report.status      = 'accepted'
            report.accepted_by = user
            report.save()

    elif action == 'reject':
        if report.status == 'pending' and role in ['ngo', 'volunteer']:
            report.status      = 'rejected'
            report.accepted_by = user
            report.save()

    elif action == 'complete':
        if role not in ['ngo', 'volunteer']:
            return HttpResponseForbidden('Only NGO/Volunteer can complete reports.')
        if report.accepted_by != user:
            return HttpResponseForbidden('Only the assigned user can complete this report.')
        if request.method == 'POST':
            proof_file = request.FILES.get('proof')
            if proof_file:
                report.proof  = proof_file
                report.status = 'completed'
                report.save()
            else:
                return render(request, 'report_detail.html',
                              {'report': report, 'proof_error': 'Please upload a proof file.'})

    return redirect('report_detail', report_id=report_id)
