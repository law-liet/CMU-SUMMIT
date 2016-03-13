from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Main/index.html')

def register(request):
    return render(request, 'Main/register.html')

def panelist(request):
    return render(request, 'Main/panelist.html')

def feature_events(request, event = 'lunch-event'):
    return render(request, 'Main/featured_events.html', {'event' : event})