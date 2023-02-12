from rest_framework import generics, permissions
from profiles.models import Profile
from .serializers import ProfileSerializer
from drf_api_league_hub.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Return a list of all profiles ordered by 
    created at
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by("-created_at")


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update a profile only if the user is
    the owner of the profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by("-created_at")
