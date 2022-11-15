from django.shortcuts import render, redirect

from .models import Testimony, Contact, Email

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

def email_list(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Email.objects.filter(email=email):
            pass 
        else:
            emailList = Email.objects.create(email=email)
    
    return redirect('index')