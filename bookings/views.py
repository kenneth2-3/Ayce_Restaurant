from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BookingForm
from django.contrib import messages
from .models import MenuItem
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            return render(request, 'bookings/booking_success.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

@login_required
def confirmation(request):
    return render(request, 'bookings/confirmation.html')

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'bookings/user_dashboard.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_bookings')

@login_required
def book_table(request):
    # Later we'll add form logic here
    return render(request, 'bookings/booking_form.html')


@staff_member_required
def staff_dashboard(request):
    # Later we'll add overview of bookings, cancellations, etc.
    return render(request, 'bookings/staff_dashboard.html')

