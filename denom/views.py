from django.shortcuts import render, redirect
from .forms import SubcriberForm

# Create your views here.

def home(request):
# ================================================ footer subcribe form =================================
    # footerForm = SubcriberForm(request.POST)
    if request.method == 'POST':
        footerForm = SubcriberForm(request.POST)
        if footerForm.is_valid():
            footerForm.save()
            return redirect('home')
        else:
            footerForm = SubcriberForm()
    else:
        footerForm = SubcriberForm()
    context = {
        'footerForm': footerForm,
    }
    return render(request, 'denom/home.html', context)


def about(request):
# ================================================ footer subcribe form =================================
    # footerForm = SubcriberForm(request.POST)
    if request.method == 'POST':
        footerForm = SubcriberForm(request.POST)
        if footerForm.is_valid():
            footerForm.save()
            return redirect('home')
        else:
            footerForm = SubcriberForm()
    else:
        footerForm = SubcriberForm()
    context = {
        'footerForm': footerForm,
    }
    return render(request, 'denom/about.html', context)

def contact(request):
# ================================================ footer subcribe form =================================
    # footerForm = SubcriberForm(request.POST)
    if request.method == 'POST':
        footerForm = SubcriberForm(request.POST)
        if footerForm.is_valid():
            footerForm.save()
            return redirect('home')
        else:
            footerForm = SubcriberForm()
    else:
        footerForm = SubcriberForm()
    context = {
        'footerForm': footerForm,
    }
    return render(request, 'denom/contact.html', context)

def blog(request):
# ================================================ footer subcribe form =================================
    # footerForm = SubcriberForm(request.POST)
    if request.method == 'POST':
        footerForm = SubcriberForm(request.POST)
        if footerForm.is_valid():
            footerForm.save()
            return redirect('home')
        else:
            footerForm = SubcriberForm()
    else:
        footerForm = SubcriberForm()
    context = {
        'footerForm': footerForm,
    }
    return render(request, 'denom/blog.html', context)

def marriage(request):
# ================================================ footer subcribe form =================================
    # footerForm = SubcriberForm(request.POST)
    if request.method == 'POST':
        footerForm = SubcriberForm(request.POST)
        if footerForm.is_valid():
            footerForm.save()
            return redirect('home')
        else:
            footerForm = SubcriberForm()
    else:
        footerForm = SubcriberForm()
    context = {
        'footerForm': footerForm,
    }
    return render(request, 'denom/marriage.html', context)

def news(request):
# ================================================ footer subcribe form =================================
    # footerForm = SubcriberForm(request.POST)
    if request.method == 'POST':
        footerForm = SubcriberForm(request.POST)
        if footerForm.is_valid():
            footerForm.save()
            return redirect('home')
        else:
            footerForm = SubcriberForm()
    else:
        footerForm = SubcriberForm()
    context = {
        'footerForm': footerForm,
    }
    return render(request, 'denom/news.html', context)