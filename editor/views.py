from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from tracker.models import Workout, Image, Video, Note
from tracker.forms import WorkoutForm, ImageForm, VideoForm, NoteForm
from django.urls import reverse


# Create your views here.
def edit_workout(request):
    return HttpResponse("Edit workout view!")

def edit_note(request):
    id = request.GET.get('id')
    user = request.user

    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            redirect_url = reverse('viewer:view_note') + '?id={}'.format(id)
            return redirect(redirect_url)
    else:
        form = NoteForm(instance=note)
    
    return render(request, 'editor/edit_note.html', {'form': form})