from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from sand_castles.permissions import IsOwnerOrReadOnly
from .models import Listing, Ratings
from .serializers import ListingSerializer


class ListingsList(generics.ListCreateAPIView):
    """
    List listings or create a listing with if logged in.
    """
    serializer_class = ListingSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
    )
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'listing_owner',
        'listing_country',
        'listing_city',

    ]
    ordering_fields = [
        'favourites_count',
        'created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(listing_owner=self.request.user.profile)


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrive a listing and edit or delete if owner
    """
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Listing.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
    )
