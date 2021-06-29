from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        complaint = request.POST['complaint']
        if len(name)<6  or len(phone)<10 or len(email)<3 or len(complaint)<8:
            messages.error(request, "One or more fields have an error. Please check and try again.")
        else:
            contact = Contact(name=name, phone=phone, email=email, content=complaint)
            contact.save()
            messages.success(request,"Your Complaint has been successfully submitted.")
    return render(request, 'home/contact.html')

def notice(request):    
    return render(request,'home/notice.html')
