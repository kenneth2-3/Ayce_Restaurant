from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput, TimeInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['email', 'phone', 'date', 'time', 'guests', 'table', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'special_requests': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any special requests?'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        guests = cleaned_data.get('guests')

        if date and time:
            booking_datetime = dt_datetime.combine(date, time)
            now = dt_datetime.now()
            if booking_datetime < now:
                raise forms.ValidationError("Booking date and time cannot be in the past.")

        if table and date and time:
            existing = Booking.objects.filter(table=table, date=date, time=time)
            if existing.exists():
                raise forms.ValidationError("This table is already booked for the selected date and time.")

        if table and guests and hasattr(table, 'capacity') and guests > table.capacity:
            raise forms.ValidationError(f"The selected table can only accommodate up to {table.capacity} guests.")

        return cleaned_data
