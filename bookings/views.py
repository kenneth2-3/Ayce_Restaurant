from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import MenuItem
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'bookings/home.html')

def menu(request):
    items = MenuItem.objects.filter(available=True)
    return render(request, 'bookings/menu.html', {'items': items})

@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

@login_required
def booking_confirmation(request):
    return render(request, 'bookings/confirmation.html')
