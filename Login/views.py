# views.py
from django.shortcuts import render

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

people = []  # List to store Person instances

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)
    return render(request, 'Login/add.html')

def show_people(request):
    return render(request, 'Login/show.html', {'people': people})
