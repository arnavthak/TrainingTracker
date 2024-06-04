from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    date = models.DateField()
    note = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", null=True)

    def __str__(self):
        return f"{self.note}"

class Workout(models.Model):
    date = models.DateField()
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts", null=True)

    def __str__(self):
        return self.description
    
class Image(models.Model):
    workout = models.ForeignKey(Workout, related_name='images', on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images", null=True)

    def __str__(self):
        return self.caption if self.caption else "No Caption"
    
class Video(models.Model):
    workout = models.ForeignKey(Workout, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos", null=True)

    def __str__(self):
        return self.caption if self.caption else "No Caption"