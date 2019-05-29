from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from events.models import Event, Category
from events.forms import EventForm
from iqbusiness.utils import send_email

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'event_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        events = super(EventListView, self).get_context_data(**kwargs)
        events['category_list'] = Category.objects.all()
        return events
    def get_queryset(self):
        return self.model.objects.all().order_by('date')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'

    def get_context_data(self, **kwargs):
        events = super(EventDetailView, self).get_context_data(**kwargs)
        events['related_event'] = Event.objects.filter(category=events['event'].category).exclude(pk=events['event'].pk)[:4]
        return events

class EventFormView(FormView):
    form_class = EventForm
    template_name = 'events/event_form.html'

    def get_context_data(self, **kwargs):
        event = super(EventFormView, self).get_context_data(**kwargs)
        event['event'] = Event.objects.get(slug=self.kwargs['slug'])
        return event

    def form_valid(self, form):
        form.cleaned_data['event'] = Event.objects.get(slug=self.kwargs['slug'])
        mail = self.send_mail(form.cleaned_data)
        if mail:
            form.save()
            return redirect('events:event_detail', slug=self.kwargs['slug'])
        else:
            return redirect('events:event_form', slug=self.kwargs['slug'])


    def send_mail(self, valid_data):
        sent = send_email('Attendee Information', 'support@iqbusiness.events' , ['bochiegfx@gmail.com'], 'includes/mail_templates/attendee_template.html', valid_data)
        return sent




def html_to_pdf_view(request):

    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('includes/mail_templates/application_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response
