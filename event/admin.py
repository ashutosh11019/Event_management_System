from django.contrib import admin

# Register your models here.
from .models import Event, Participant, registration

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(registration)