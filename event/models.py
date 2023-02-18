from django.db import models

# Create your models here.

EVENT_CHOICE = {
    ('Virtual', 'Virtual'),
    ('On-Premise', 'On-Premise'),
}

EVENT_STATUS_CHOICE = {
    ('Live', 'Live'),
    ('Scheduled', 'Scheduled'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
}

class Event(models.Model):
    event_id = models.CharField(max_length=4)
    event_name = models.CharField(max_length=20)
    event_date = models.DateField()
    organizer_email = models.CharField(max_length=50)
    organizer_phone = models.CharField(max_length=10)
    event_description = models.CharField(max_length=100)
    event_type = models.CharField(choices=EVENT_CHOICE, max_length=15)
    event_location = models.CharField(max_length=20)
    event_status = models.CharField(choices=EVENT_STATUS_CHOICE, max_length=20)
    max_seats = models.CharField(max_length=5)

class Participant(models.Model):
    booking_id=models.CharField(max_length=4)
    event_id=models.CharField(max_length=4)
    booked_date=models.DateField()
    participant_name=models.CharField(max_length=30)
    participant_email=models.CharField(max_length=40)
    participant_phone=models.CharField(max_length=10)

class registration(models.Model):    
    participant_name=models.CharField(max_length=30)    
    participant_email=models.CharField(max_length=40)    
    participant_phone=models.IntegerField()    
    participant_password=models.CharField(max_length=20)
