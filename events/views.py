from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, View
from events.models import Event, Category
from events.forms import EventForm
from iqbusiness.utils import send_email
from django.utils import timezone


# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'event_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        events = super(EventListView, self).get_context_data(**kwargs)
        events['category_list'] = Category.objects.all()
        return events

    def get_queryset(self):
        return self.model.objects.all().order_by('d_from')


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'

    def get_context_data(self, **kwargs):
        events = super(EventDetailView, self).get_context_data(**kwargs)
        events['related_event'] = Event.objects.filter(
            category=events['event'].category).exclude(pk=events['event'].pk)[:4]
        return events


class EventFormView(FormView):
    form_class = EventForm
    template_name = 'events/event_form.html'

    def get_context_data(self, **kwargs):
        event = super(EventFormView, self).get_context_data(**kwargs)
        event['event'] = Event.objects.get(slug=self.kwargs['slug'])
        return event

    def form_valid(self, form):
        form.cleaned_data['event'] = Event.objects.get(
            slug=self.kwargs['slug'])
        mail = self.send_mail(form.cleaned_data)
        if mail:
            form.save()
            return redirect('events:event_detail', slug=self.kwargs['slug'])
        else:
            return redirect('events:event_form', slug=self.kwargs['slug'])

    def send_mail(self, valid_data):
        sent = send_email('Attendee Information', 'info@iqbusiness.events', [
                          'bochiegfx@gmail.com'], 'includes/mail_templates/attendee_template.html', valid_data)
        return sent


from xhtml2pdf import pisa
from io import StringIO, BytesIO
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def html_to_pdf_directly(request):
    template = get_template(
        "includes/mail_templates/attende_pdf.html")
    data = dict({'pagesize': 'A4', 'email': 'bochiegfx'})
    html = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('Errors')
