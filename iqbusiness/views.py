from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, FormView
from events.models import Event
from iqbusiness.forms import ContactForm
from django.contrib import messages
from iqbusiness.utils import send_email


# Create your views here.


class HomeView(View):
    def get(self, request):
        hello = "Hello world"
        events_list = Event.objects.all().order_by('-created_on')[:3]
        return render(request, 'home.html', {"events":events_list})

class AboutView(View):
    def get(self, request):
        hello = "Hello world"
        return render(request, 'about.html', {'hello': hello})


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        mail = self.send_mail(form.cleaned_data)
        mail = 1
        if mail:
            form.save()
            messages.success(self.request, 'Thank You for contacting us, We shall get back to you soon!')
            return redirect('contact')
        else:
            messages.error(self.request, 'Please check the details!')
            return redirect('contact')

    def send_mail(self, valid_data):
        sent = send_email('Contact Information', 'info@iqbusiness.events' , ['bochiegfx@gmail.com'], 'includes/mail_templates/contact_template.html', valid_data)
        return sent
