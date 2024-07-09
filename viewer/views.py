from django.shortcuts import render
from django.http import HttpResponse
from tracker.models import Workout, Image, Video

# Create your views here.
def view_workout(request):
    id = request.GET.get('id')
    user = request.user

    try:
        workout_instance = Workout.objects.get(id=id)
    except Workout.DoesNotExist:
        return HttpResponse("The workout object associated with id {} does not exist!".format(id))
    
    if workout_instance.created_by != user:
        return HttpResponse("The workout object associated with id {} does not belong to you!".format(id))

    description = workout_instance.description
    images = Image.objects.filter(created_by=user, workout=workout_instance)
    videos = Video.objects.filter(created_by=user, workout=workout_instance)

    return render(request, 'viewer/view_workout.html', {'description': description, 'images': images, 'videos': videos})