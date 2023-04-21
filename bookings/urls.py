from django.urls import path
from bookings import views

urlpatterns = [
    path('', views.BookingsList.as_view()),
    path('booking/<int:pk>', views.BookingDetail.as_view())
]