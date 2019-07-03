from django import forms
from events.models import ContactForm


class ContactForm(forms.ModelForm):

    # message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Message'}))


    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter Message'}),

        }
