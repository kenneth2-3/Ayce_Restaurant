from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book_table, name='book_table'),
    path('confirmation/', views.confirmation, name='booking_confirmation'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

]
