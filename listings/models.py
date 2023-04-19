from django.db import models
from django_countries.fields import CountryField

from members.models import Member


class Listing(models.model):
    AMENITIES = (
        ('Dishwasher', 'Dishwasher'),
        ('Iron', 'Iron'),
        ('Washer & Dryer', 'Washer & Dryer'),
        ('Pool', 'Pool'),
        ('Jacuzzi', 'Jacuzzi'),
        ('Coffee Machine', 'Coffee Machine'),
        ('Garden', 'Garden'),
        ('Wifi', 'Wifi'),
        ('BBQ', 'BBQ'),
        ('Pizza Oven', 'Pizza Oven'),
        ('Smart TV', 'Smart TV'),
    )
    SERVICES = (
        ('Housekeeping', 'Housekeeping'),
        ('Massage', 'Massage'),
        ('Food preparation', 'Food preparation'),
        ('Babysitting', 'Babysitting'),
        ('Airport Pickup', 'Airport Pickup'),
    )
    title = models.CharField(max_length=25, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    image_primary = models.Image
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    listing_city = models.CharField(max_length=20, null=False, blank=False)
    listing_country = models.CountryField(max_length=20, null=False,
                                          blank=False)
    listing_owner = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='listings')
    ratings = models.OneToManyField(Ratings, null=True, blank=True)
    bedrooms = models.IntegerField()
    max_occupancy = models.IntegerField()
    amenities = models.CharField(choices=AMENITIES)
    available_services = models.Charfield(choices=SERVICES, null=True,
                                          blank=True)
    favourites = models.ManyToManyField(Profile, related_name='favourite',
                                        blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def favourites_count(self):
        return self.favourites.count()

    def bookings_count(self):
        return self.bookings.count()


class Ratings(models.Model):
    SATISFACTION_OPTIONS = (
        (1, "Dream vacation"),
        (2, "Excellent"),
        (3, "Very good"),
        (4, "Good"),
        (5, "Not as expected"),
        (6, "Bad experience"),
    )
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    review = models.TextField(null=False, Blank=False, Default="")
    satisfaction = models.CharField(max_length=50,
                                    choices=SATISFACTION_OPTIONS)
