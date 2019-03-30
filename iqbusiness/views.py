from django.shortcuts import render
from .data import events

# Create your views here.

def home(request):
    hello = "Hello world"
    events_list = events


    return render(request, 'home.html', {'hello': hello, 'events':events_list})
