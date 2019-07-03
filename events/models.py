from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from iqbusiness.utils import unique_slug_generator, RandomFileName

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name



class Event(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to=RandomFileName('Event'), null=True, blank=True)
    pdf = models.FileField(upload_to=RandomFileName('EventPdf'), null=True, blank=True)
    venue = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField( null=True, blank=True)
    d_from = models.DateField()
    d_to = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class EventForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name





def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)


pre_save.connect(slug_save, sender=Event)
