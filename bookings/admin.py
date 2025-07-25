from django.contrib import admin
from .models import Table, Booking, MenuItem
from django.utils.html import format_html


# Register your models here.

admin.site.register(Table)
admin.site.register(Booking)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50"/>', obj.image.url)
        return '-'
    image_tag.short_description = 'Image'
