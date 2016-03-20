from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from models import User
from django.http import JsonResponse
from django.shortcuts import redirect


def redirectHttps(request):
    temp = 'www.cmu-summit.com' + request.path
    return redirect('https://' + temp, permanent=True)

def index(request):
    if (request.is_secure()):
        return render(request, 'Main/index.html')
    else:
        return redirectHttps(request)        


def register(request):
    if (request.is_secure()):
        return render(request, 'Main/register.html')
    else:
        return redirectHttps(request)  

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