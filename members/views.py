from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    def get(self, request):
        members = Profile.objects.all()
        serializer = ProfileSerializer(members, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    serializer_class = ProfileSerializer

    def get_object(self, pk):
        try:
            member = Profile.objects.get(pk=pk)
            return member
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = ProfileSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        member = self.get_object(pk)
        serializer = ProfileSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
