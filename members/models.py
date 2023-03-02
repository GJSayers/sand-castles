from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField
from django_countries.fields import CountryField


class Profile(models.Model):
    """
    Creates a member profile, a member can be both host and a guest user.
    """
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=42, null=False)
    email_address = models.EmailField(max_length=150, null=False)
    phone_number = models.CharField(max_length=20, null=True)
    address_1 = models.CharField(max_length=80, null=True)
    address_2 = models.CharField(max_length=80, null=True)
    city = models.CharField(max_length=40, null=True)
    postcode = models.CharField(max_length=12, null=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    group_size = models.PositiveSmallIntegerField(null=True)
    PREFERENCE_OPTIONS = (
        (1, 'Quiet Location'),
        (2, 'By the Sea'),
        (3, 'Swimming Pool'),
        (4, 'Pet Friendly'),
        (5, 'Family Friendly'),
        (6, 'Couples'),
        (7, 'City Life'),
        (8, 'Outdoor Space'),
    )
    preferences = MultiSelectField(
        max_length=100, blank=True, choices=PREFERENCE_OPTIONS
        )
    is_host = models.BooleanField(null=True)
    is_guest = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../'
    )

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.member}'s profile"


@receiver(post_save, sender=User)
def create_or_update_member(sender, instance, created, **kwargs):
    """
    Create / Update member profile
    """
    if created:
        Profile.objects.create(member=instance)
    # Existing users save the updated profile if any changes are made
    instance.profile.save()
