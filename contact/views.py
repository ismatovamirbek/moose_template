from django.shortcuts import render, redirect
from .forms import ContactForm,SubscriptionForm



def contact(request):
    form = ContactForm(request.POST or None)
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")

    if form.is_valid():
        form.save()
        return redirect(".")

    context ={
        'form': form,
        "sub": sub
    }

    return render(request, 'contact.html', context)