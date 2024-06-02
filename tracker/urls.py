from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path("", views.index, name="index"),
    path('add_training/', views.add_training, name='add_training'),
]