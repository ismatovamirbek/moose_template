from django.shortcuts import render, redirect
from contact.forms import SubscriptionForm
from .models import Blog, Tag, Comment
from .forms import CommentForm
from django.core.paginator import Paginator


def index(request):
    sub = SubscriptionForm(request.POST or None)
    blogs = Blog.objects.all().order_by("-id")[:2]
    if sub.is_valid():
        sub.save()
        return redirect(".")

    ctx = {
        "sub": sub,
        "blogs": blogs
    }

    return render(request, "index.html", ctx)


def blog(request):
    b = Blog.objects.all().order_by('-id')
    p = Paginator(b, 2)
    page = request.GET.get("page")
    blog = p.get_page(page)
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")
    ctx = {
        'blogs': blog,
        "sub": sub
    }

    return render(request, 'blog.html', ctx)

def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        com = comment.save(commit=False)
        com.blog = blog
        com.save()
        return redirect(".")
    sub = SubscriptionForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        return redirect(".")


    ctx = {
        "blog": blog,
        "comment": comment,
        "sub": sub
    }

    return render(request, 'blog-single.html', ctx)