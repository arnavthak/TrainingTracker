from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from tracker.models import Workout, Image, Video, Note
from tracker.forms import WorkoutForm, VideoInlineFormSet, ImageInlineFormSet, NoteForm
from django.urls import reverse


# Create your views here.
def edit_workout(request):
    id = request.GET.get('id')
    user = request.user
    
    workout = get_object_or_404(Workout, id=id)
    if workout.created_by != user:
        return render(request, 'editor/cannot_access.html')
    
    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST, instance=workout)
        image_formset = ImageInlineFormSet(request.POST, request.FILES, instance=workout)
        video_formset = VideoInlineFormSet(request.POST, request.FILES, instance=workout)
        if workout_form.is_valid() and image_formset.is_valid() and video_formset.is_valid():
            workout_form.save()
            image_formset.save()
            video_formset.save()
            redirect_url = reverse('viewer:view_workout') + '?id={}'.format(id)
            return redirect(redirect_url)
    else:
        workout_form = WorkoutForm(instance=workout)
        image_formset = ImageInlineFormSet(instance=workout)
        video_formset = VideoInlineFormSet(instance=workout)

    return render(request, 'editor/edit_workout.html', {
        'workout_form': workout_form,
        'image_formset': image_formset,
        'video_formset': video_formset
    })

def edit_note(request):
    id = request.GET.get('id')
    user = request.user

    note = get_object_or_404(Note, id=id)
    if note.created_by != user:
        return render(request, 'editor/cannot_access.html')

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            redirect_url = reverse('viewer:view_note') + '?id={}'.format(id)
            return redirect(redirect_url)
    else:
        form = NoteForm(instance=note)
    
    return render(request, 'editor/edit_note.html', {'form': form})