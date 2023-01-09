from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'denom/home.html')


def about(request):
    return render(request, 'denom/about.html')

def contact(request):
    return render(request, 'denom/contact.html')

def blog(request):
    return render(request, 'denom/blog.html')

def marriage(request):
    return render(request, 'denom/marriage.html')

def news(request):
    return render(request, 'denom/news.html')