from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path("", views.index, name="index"),
    path('add_training/', views.add_training, name='add_training'),
    path('add_training/add_workout/', views.add_workout, name='add_workout'),
    path('add_training/add_note', views.add_note, name='add_note'),
]