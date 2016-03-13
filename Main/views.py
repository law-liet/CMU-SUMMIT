from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from models import User

def index(request):
    return render(request, 'Main/index.html')

def register(request):
    return render(request, 'Main/register.html')

def panelist(request):
    return render(request, 'Main/panelist.html')

def feature_events(request, event = 'lunch-event'):
    return render(request, 'Main/featured_events.html', {'event' : event})

def signup(request):
    data = request.POST
    email = data['email']
    try:
        User.objects.get(email=email)
        return "Email alreday exists"
    except ObjectDoesNotExist:
        name = data['name']
        phone = data['phone']
        company = data['company']
        role = data['role']
        user = User.objects.create(name=name, email=email, phone=phone, company=company, role=role)
        user.save()

def about_us(request):
    return render(request, 'Main/about_us.html')