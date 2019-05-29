from django import forms
from events.models import EventForm


class EventForm(forms.ModelForm):

    class Meta:
        model = EventForm
        fields = ['first_name', 'last_name', 'email', 'phone', 'organization']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'organization': forms.TextInput(attrs={'placeholder': 'Enter Organization Name'}),


        }
