from django.utils.text import slugify
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)

def unique_slug_generator(model_instance, title, slug_field):
    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1
        slug = f'{slug}-{object_pk}'

    return slug

def send_email(subject, mail_from, to_emails, template, data):

    subject = subject
    html_message = render_to_string(template, {'data': data})
    plain_message = strip_tags(html_message)

    from_email = 'IQ Business <{}>'.format(mail_from)
    send_mail = mail.send_mail(subject, plain_message, from_email, to_emails, html_message=html_message, fail_silently=False)

    return send_mail
