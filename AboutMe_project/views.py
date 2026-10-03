from django.shortcuts import render
from AMapp.models import AMapp
from ContactUsapp.models import ContactUs, MassageMe


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        MassageMe.objects.create(name=name, email=email, subject=subject, message=message)


    AMapps = AMapp.objects.all()
    ContactUss = ContactUs.objects.all().last()

    return render(request, 'index.html', {'AMapps': AMapps ,'ContactUss':ContactUss})

