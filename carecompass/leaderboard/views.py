from django.db.models import Count, Q
from django.shortcuts import render
from user.models import CustomUser

def leaderboard(request):

    # Top Users – based on submitted reports

    top_users = CustomUser.objects.filter(role="user").annotate(
        count=Count("reports")  # 'reports' হলো Report মডেলের related_name
    ).order_by("-count")[:10]


    # Top Volunteers – based on completed accepted reports

    top_volunteers = CustomUser.objects.filter(role="volunteer").annotate(
        count=Count("accepted_reports", filter=Q(accepted_reports__status="completed"))
    ).order_by("-count")[:10]


    # Top NGOs – based on completed accepted reports

    top_ngos = CustomUser.objects.filter(role="ngo").annotate(
        count=Count("accepted_reports", filter=Q(accepted_reports__status="completed"))
    ).order_by("-count")[:10]

    context = {
        "top_users": top_users,
        "top_volunteers": top_volunteers,
        "top_ngos": top_ngos,
    }

    return render(request, "leaderboard.html", context)
