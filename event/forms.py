from django import forms
from .models import *

class MyParticipant(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

class MyEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class MyRegistration(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'


