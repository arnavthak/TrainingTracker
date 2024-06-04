from django.contrib import admin

# Register your models here.
from .models import Workout, Image, Video

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VideoInline]

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Image)
admin.site.register(Video)