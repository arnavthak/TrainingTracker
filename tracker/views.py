from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'tracker/calendar.html')

def add_training(request):
    date = request.GET.get('date')
    if date:
        return render(request, 'tracker/add_training.html', {'date': date})
    else:
        return render(request, 'tracker/no_date_provided.html')