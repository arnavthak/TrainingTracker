from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'tracker/calendar.html')

def add_training(request):
    date = request.GET.get('date')
    if date:
        return HttpResponse(f"{date}")
    else:
        return HttpResponse("Could not access date data")