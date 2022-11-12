from django.shortcuts import render, redirect

from .models import Testimony, Contact

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact  = Contact.objects.create(name=name, email=email, message=message)     
        
    testimonies = Testimony.objects.filter(is_approved=True)
    context = {
        "testimonies":testimonies,
    }
            
    return render(request, 'index.html', context)