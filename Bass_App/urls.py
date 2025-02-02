from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),  
    path('booking/', views.book_ride, name='book_ride'),  
    path('contact/', views.contact, name='contact'),  
]