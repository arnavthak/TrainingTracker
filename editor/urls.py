from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path("edit_workout", views.edit_workout, name="edit_workout"),
    path("edit_note", views.edit_note, name="edit_note"),
]