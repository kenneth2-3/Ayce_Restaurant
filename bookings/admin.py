from django.contrib import admin
from .models import Table, Booking, MenuItem


# Register your models here.

admin.site.register(Table)
admin.site.register(Booking)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
