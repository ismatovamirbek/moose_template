from django.shortcuts import render, redirect

from contact.forms import SubscriptionForm
from .models import About



def about(request):
    about = About.objects.all()
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    context = {
        'about': about,
        "sub": sub
    }

    return render(request, "about.html", context)