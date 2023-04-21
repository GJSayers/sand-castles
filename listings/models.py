from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.utils.text import slugify

from members.models import Profile


class Listing(models.Model):
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
    image_primary = models.ImageField(null=True)
    image_secondary = models.ImageField(null=True)
    image_tertiary = models.ImageField(null=True)
    image_url_primary = models.URLField(null=True)
    image_url_secondary = models.URLField(null=True)
    image_url_tertiary = models.URLField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    listing_city = models.CharField(max_length=20, null=False, blank=False)
    listing_country = CountryField(max_length=20, null=False,
                                   blank=False)
    listing_owner = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                      null=True, blank=True,
                                      related_name='listings')
    bedrooms = models.IntegerField()
    max_occupancy = models.IntegerField()
    amenities = MultiSelectField(max_length=200, choices=AMENITIES)
    available_services = MultiSelectField(max_length=200, choices=SERVICES,
                                          null=True,
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, **kwargs)


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
    review = models.TextField(null=False, blank=False, default="")
    satisfaction = models.CharField(max_length=50,
                                    choices=SATISFACTION_OPTIONS)
