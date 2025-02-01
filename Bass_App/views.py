from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request,'index.html')

def ContactView(request):
    return render(request,'contact.html')

def BookingView(request):
    return render(request,'booking.html')
