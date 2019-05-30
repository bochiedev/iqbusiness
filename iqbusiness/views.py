from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from events.models import Event

# Create your views here.

class HomeView(View):
    def get(self, request):
        hello = "Hello world"
        events_list = Event.objects.all().order_by('-date_from')[:3]
        return render(request, 'home.html', {'hello': hello, 'events':events_list})

class AboutView(View):
    def get(self, request):
        hello = "Hello world"
        return render(request, 'about.html', {'hello': hello})

class ContactView(View):
    def get(self, request):
        hello = "Hello world"

        return render(request, 'contact.html', {'hello': hello})
