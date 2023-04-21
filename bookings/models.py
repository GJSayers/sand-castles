import uuid

from django.db import models
from django_countries.fields import CountryField

from listings.models import Listing
from members.models import Profile


class Booking(models.Model):
    booking_number = models.CharField(max_length=32, null=False,
                                      editable=False)
    booking_member = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                       null=True, blank=True,
                                       related_name="bookings")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=False,
                                  editable=True, blank=True, null=True)
    end_date = models.DateField(auto_now_add=False,
                                editable=True, blank=True, null=True)

    def _generate_booking_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.booking_number
