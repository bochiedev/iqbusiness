from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "events"

urlpatterns = [
    path('', EventListView.as_view(), name="event_list" ),
    path('<slug:slug>', EventDetailView.as_view(), name="event_detail" ),
    path('event/<slug:slug>', EventFormView.as_view(), name="event_form" ),


    path('pdf/<int:pk>', MyModelImageView.as_view(), name="pdf" ),



]
