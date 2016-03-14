from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from models import User
from django.http import JsonResponse

def index(request):
    return render(request, 'Main/index.html')

def register(request):
    return render(request, 'Main/register.html')

def panelist(request):
    return render(request, 'Main/panelist.html')

def feature_events(request, event = 'lunch-event'):
    return render(request, 'Main/featured_events.html', {'event' : event})

def signup(request):

    email = request.POST['email']
    try:
        User.objects.get(email=email)
        return "Email alreday exists"
    except ObjectDoesNotExist:
        name = request.POST['name']
        phone = request.POST['phone']
        company = request.POST['company']
        role = request.POST['role']
        user = User.objects.create(name=name, email=email, phone=phone, interested_company=company, role=role)
        user.save()
        return JsonResponse({'status': 0})

def about_us(request):
    return render(request, 'Main/about_us.html')