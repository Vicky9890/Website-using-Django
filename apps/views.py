from django.shortcuts import render, HttpResponse
from datetime import datetime
from apps.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    content={
        "variable1":"Vikash Kumar Pradhan",
        "variable2":"Rohan Kumar"
    }
    return render(request, "form.html", content)

def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is my about page")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is my services page")

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        text = request.POST.get("text")
        contact = Contact(name=name, email=email, phone=phone, text=text, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
        
    return render(request, "contact.html")
    # return HttpResponse("This is my contact page")

    