from rest_framework import serializers
from django.utils.text import slugify
from .models import Listing, Ratings


class ListingSerializer(serializers.ModelSerializer):
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
    listing_owner = serializers.ReadOnlyField(source='listing_owner.Profile')
    is_host = serializers.SerializerMethodField()
    is_guest = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='listing_owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='listing_owner.profile.image.url')
    favourites_count = serializers.ReadOnlyField()
    amenities = serializers.MultipleChoiceField(choices=AMENITIES)
    available_services = serializers.MultipleChoiceField(choices=SERVICES)
    slug = serializers.SlugField(required=False)

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.listing_owner.profile
    
    def get_is_host(self, obj):
        request = self.context['request']
        return request.user == obj.listing_owner.is_host
    
    def get_is_guest(self, obj):
        request = self.context['request']
        return request.user == obj.listing_owner.is_guest
    
    


    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'listing_owner', 'is_host',
            'is_guest', 'profile_id',
            'profile_image', 'created_on',
            'title', 'image_primary', 'image_secondary',
            'image_tertiary', 'published', 'listing_city',
            'listing_country', 'bedrooms', 'max_occupancy',
            'amenities', 'available_services', 'favourites_count', 'slug',
        ]
