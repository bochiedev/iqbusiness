from django.contrib import admin
from events.models import Event, Category, EventForm

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'venue', 'category', 'd_from', 'd_to' , 'created_by', 'created_on', 'image']
    list_filter = ['category', 'd_from', 'created_by', 'venue']
    list_editable = ['category']
    date_hierarchy = 'd_from'

admin.site.register(Event, EventAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']

admin.site.register(Category, CategoryAdmin)

class EventFormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'organization', 'created_on']
    list_filter = ['organization', 'created_on']
    date_hierarchy = 'created_on'
admin.site.register(EventForm, EventFormAdmin)
