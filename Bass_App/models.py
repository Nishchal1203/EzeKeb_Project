from django.db import models

# Create your models here.

# Define common location choices


class Booking(models.Model):
    LOCATION_CHOICES = [
    ('Jaipur', 'Jaipur'),
    ('Khatu Shyam', 'Khatu Shyam'),
    ('Ajmer', 'Ajmer'),
    ('Salasar', 'Salasar'),
    ('Jaipur Junction', 'Jaipur Junction'),
    ('Jaipur Darshan', 'Jaipur Darshan'),
    ('Dausa', 'Dausa'),
    ('Behroad', 'Behroad'),
    ('Other', 'Other'),
]
    starting_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    destination = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    phone_no = models.CharField(max_length=10)
    num_travelers = models.IntegerField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking from {self.starting_location} to {self.destination}"
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
