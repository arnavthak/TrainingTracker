from django.shortcuts import render
from django.http import HttpResponse
from .models import Workout, Note, Image, Video

# Create your views here.
def index(request):
    return render(request, 'tracker/calendar.html')

def add_training(request):
    date = request.GET.get('date')
    user = request.user
    year, month, day = date.split('-')
    if date:
        workouts = Workout.objects.filter(date=date, created_by=user)
        notes = Note.objects.filter(date=date, created_by=user)
        return render(request, 'tracker/add_training.html', {'date': date, 'workouts': workouts, 'notes': notes})
    else:
        return render(request, 'tracker/no_date_provided.html')