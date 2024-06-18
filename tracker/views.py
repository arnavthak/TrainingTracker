from django.shortcuts import render
from django.http import HttpResponse
from .models import Workout, Note, Image, Video
from .forms import WorkoutForm, NoteForm, VideoInlineFormSet, ImageInlineFormSet

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

def add_workout(request):
    #return HttpResponse("You are seeing the add_workout view")
    #return render(request, 'tracker/add_workout.html')
    # form = WorkoutForm(request.POST, request.FILES)

    # if form.is_valid():
    #     form.save()
    
    # return render(request, 'tracker/add_workout.html', {'form': form})
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        video_formset = VideoInlineFormSet(request.POST, request.FILES, instance=Workout())
        image_formset = ImageInlineFormSet(request.POST, request.FILES, instance=Workout())
        
        if form.is_valid() and video_formset.is_valid() and image_formset.is_valid():
            workout = form.save(commit=False)
            workout.created_by = request.user 
            workout.date = request.GET.get('date')
            workout.save()
            
            video_formset.instance = workout
            image_formset.instance = workout
            video_formset.save()
            image_formset.save()
            return HttpResponse("Workout saved successfully!")
    else:
        form = WorkoutForm()
        video_formset = VideoInlineFormSet(instance=Workout())
        image_formset = ImageInlineFormSet(instance=Workout())
    
    return render(request, 'tracker/add_workout.html', {
        'form': form,
        'video_formset': video_formset,
        'image_formset': image_formset,
    })

def add_note(request):
    #return HttpResponse("You are seeing the add_note view")
    #return render(request, 'tracker/add_note.html')
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.date = request.GET.get('date')
            note.created_by = request.user
            note.save()
            return HttpResponse("Note saved successfully!")
    else:
        form = NoteForm()
    return render(request, 'tracker/add_note.html', {'form': form})