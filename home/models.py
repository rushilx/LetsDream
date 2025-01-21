from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    LOCATION_CHOICES = [
        ('chandigarh', 'sector 43'),
        ('mohali', 'punjab'),
        ('location3', 'Location 3'),
    ]

    CAR_CHOICES = [
        ('scoda', 'm24'),
        ('bmw', 'c22'),
        ('car3', 'Car Model 3'),
    ]

    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    date = models.DateField()
    car = models.CharField(max_length=100, choices=CAR_CHOICES)
    
    def __str__(self):
        return f"Booking: {self.location} - {self.car} - {self.date}"
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question    

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status_choices = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket: {self.subject} ({self.status})"
