from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from models import User
from django.http import JsonResponse
from django.shortcuts import redirect


def redirectHttps(request):
    temp = 'www.cmu-summit.com' + request.path
    return redirect('https://' + temp, permanent=True)

def index(request):
    #if (request.is_secure()):
    return render(request, 'Main/index.html')
    #else:
    #return redirectHttps(request)        


def register(request):
    #if (request.is_secure()):
    return render(request, 'Main/register.html')
    #else:
    #return redirectHttps(request)  
def agenda(request):
    return render(request, 'Main/agenda.html')

def keynote_speakers(request):
    return render(request, 'Main/keynote_speakers.html')

def opening_remarks(request):
    return render(request, 'Main/opening_remarks.html')

def ie(request):
    return render(request, 'Main/ie.html')

def sustainability(request):
    return render(request, 'Main/sustainability.html')

def finance(request):
    return render(request, 'Main/finance.html')

def start_up(request):
    return render(request, 'Main/start_up.html')

def high_tech(request):
    return render(request, 'Main/high_tech.html')

def competition(request):
    return render(request, 'Main/competition.html')

def collaborators(request):
    return render(request, 'Main/collaborators.html')

def panelist(request):
    return render(request, 'Main/panelist.html')

def feature_events(request):
    return render(request, 'Main/featured_events.html')

def job_fair(request):
    return render(request, 'Main/job_fair.html')

def register_job(request):
    return render(request, 'Main/register_job.html')

def career(request):
    return render(request, 'Main/career.html')

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
        degree= request.POST['degree']
        major = request.POST['major']
        user = User.objects.create(name=name, email=email, role=role , degree= degree, major= major)
        user.save()
        return JsonResponse({'status': 0})

def about_us(request):
    return render(request, 'Main/about_us.html')

def test(request):
    return render(request, 'Main/events_register.html')    