from django.shortcuts import render
from projects_app.models import Project
from contactus_app.models import Footer , Message

def home(request):
    footers = Footer.objects.all().last()
    return  render(request , 'index.html' , context={'footers' : footers})

def temp_home(request):
    return render(request , 'index.html' , context={})

def about(request):
    return render(request , 'about.html' , context={})

def temp_about(request):
    return render(request , 'about.html' , context={})

def client(request):
    return render(request , 'clients.html' , context={})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        Message.objects.create(name=name , email=email , phone=phone , text=text)

    footers = Footer.objects.all().last()
    return render(request , 'contact.html' , context={'footers' : footers})

def project(request):
    projects = Project.objects.all()
    return render(request , 'projects.html' , context={'projects' : projects})

