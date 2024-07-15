from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def edit_workout(request):
    return HttpResponse("Edit workout view!")

def edit_note(request):
    return HttpResponse("Edit note view!")