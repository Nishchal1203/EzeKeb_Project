from django import forms
from .models import Booking
from .models import Contact

class BookingForm(forms.ModelForm):
    starting_location = forms.ChoiceField(choices=Booking.LOCATION_CHOICES)
    destination = forms.ChoiceField(choices=Booking.LOCATION_CHOICES)
    pickup_date = forms.DateField(widget=forms.SelectDateWidget)  # Dropdown for Date
    pickup_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Dropdown for Time
    class Meta:
        model = Booking
        fields = '__all__'
        
    

    starting_location = forms.ChoiceField(choices=Booking.LOCATION_CHOICES)
    destination = forms.ChoiceField(choices=Booking.LOCATION_CHOICES)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # Include all fields