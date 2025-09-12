from django.db.models import Count, Q
from django.shortcuts import render
from user.models import CustomUser

def leaderboard(request):
    top_users = CustomUser.objects.filter(role="user").annotate(count=Count("reports")).order_by("-count")[:10]
    top_volunteers = CustomUser.objects.filter(role="volunteer").annotate(count=Count("accepted_reports", filter=Q(accepted_reports__status="completed"))).order_by("-count")[:10]
    top_ngos = CustomUser.objects.filter(role="ngo").annotate(count=Count("accepted_reports", filter=Q(accepted_reports__status="completed"))).order_by("-count")[:10]

    return render(request, "leaderboard.html", {
        "top_users": top_users,
        "top_volunteers": top_volunteers,
        "top_ngos": top_ngos,
    })
