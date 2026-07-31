from django.shortcuts import render
from report.models import Report
from user.models import CustomUser

def home(request):
    stats = {
        'reports':   Report.objects.count(),
        'volunteers': CustomUser.objects.filter(role='volunteer').count(),
        'ngos':       CustomUser.objects.filter(role='ngo').count(),
        'completed':  Report.objects.filter(status='completed').count(),
    }
    recent_reports = Report.objects.filter(
        status__in=['pending','accepted']
    ).order_by('-created_at')[:3]
    return render(request, 'home.html', {
        'stats': stats,
        'recent_reports': recent_reports,
    })
