from rest_framework import serializers
from .models import Profile
from django_countries.serializer_fields import CountryField



class ProfileSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    country = CountryField()

    class Meta:
        model = Profile
        fields = [
            'id', 'member', 'name', 'email_address', 'phone_number',
            'address_1', 'address_2', 'city', 'country', 'postcode',
            'group_size', 'preferences', 'is_host', 'is_guest',
            'created_date', 'last_updated', 'image',
            ]
