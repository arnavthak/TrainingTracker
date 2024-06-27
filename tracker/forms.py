from django.forms import ModelForm
from .models import Workout, Note, Video, Image
from django.forms.models import inlineformset_factory

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ["description"]

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note"]

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['video_file', 'caption']

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image_file', 'caption']

# Inline formsets
VideoInlineFormSet = inlineformset_factory(Workout, Video, form=VideoForm, extra=1, can_delete=False)
ImageInlineFormSet = inlineformset_factory(Workout, Image, form=ImageForm, extra=1, can_delete=False)