from django.urls import path
from . import views
from .views import add_person, show_people

urlpatterns = [
    path('add/', add_person, name='add_person'),
    path('', show_people, name='show_people'),
]