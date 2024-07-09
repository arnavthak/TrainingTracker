from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path("view_workout", views.view_workout, name="view_workout"),
    path("view_note", views.view_note, name="view_note"),
]