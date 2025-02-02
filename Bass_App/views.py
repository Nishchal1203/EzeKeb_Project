from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm ,BookingForm
from .models import Booking

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def book_ride(request):
    return render(request,'booking.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def book_ride(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect('book_ride')  
        else:
            messages.error(request, "There was an error in your booking. Please try again.")
    else:
        form = BookingForm()  

    return render(request, 'booking.html', {'form': form}) 