from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from sand_castles.permissions import IsOwnerOrReadOnly
from .models import Booking
# from .serializers import BookingSerializer


class BookingsList(generics.ListCreateAPIView):
    """
    List listings or create a listing with if logged in.
    """
    serializer_class = BookingSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Booking.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'booking_member',
        'booking_number',
        'booking_date',
        'start_date',
        'end_date',
    ]

    ordering_fields = [
        'start_date',
        'booking_date',
    ]

    def perform_create(self, serializer):
        serializer.save(booking_member=self.request.user.profile)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrive a listing and edit or delete if owner
    """
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrReadOnly]

