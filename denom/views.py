from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Subcriber, Contact

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'denom/home.html', context)


def about(request):
    context = {

    }
    return render(request, 'denom/about.html', context)

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home')
        else:
            print('An error occurred')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form
    }
    return render(request, 'denom/contact.html', context)



def blog(request):
    context = {

    }
    return render(request, 'denom/blog.html', context)

def marriage(request):
    context = {
    
    }
    return render(request, 'denom/marriage.html', context)

def news(request):
    context = {
        
    }
    return render(request, 'denom/news.html', context)

def footer(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subcriber.objects.create(email=email)
        return redirect(request.META.get('HTTP_REFERER'))
        
def feedback(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(
            first_name=full_name,
            phone_number=phone_number,
            email=email,
            message=message
        )
        return redirect(request.META.get('HTTP_REFERER'))