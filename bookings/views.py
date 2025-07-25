from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import BookingForm
from itertools import groupby
from operator import attrgetter
from .models import MenuItem
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def home(request):
    return render(request, 'bookings/home.html')

def menu(request):
    items = MenuItem.objects.all().order_by('category', 'name')
    grouped_items = {}
    for category, group in groupby(items, key=attrgetter('category')):
        grouped_items[category] = list(group)

    return render(request, 'bookings/menu.html', {'grouped_items': grouped_items})

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

@staff_member_required
def staff_dashboard(request):
    # Later we'll add overview of bookings, cancellations, etc.
    return render(request, 'bookings/staff_dashboard.html')

