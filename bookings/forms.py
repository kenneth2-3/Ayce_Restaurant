from django import forms
from .models import Booking
from django.forms.widgets import DateInput, TimeInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['email', 'phone', 'date', 'time', 'guests', 'table', 'special_requests']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'special_requests': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any special requests?'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if table and date and time:
            # Check for double booking
            existing = Booking.objects.filter(table=table, date=date, time=time)
            if existing.exists():
                raise forms.ValidationError("This table is already booked for the selected date and time.")
