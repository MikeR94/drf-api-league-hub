from rest_framework import generics, permissions
from profiles.models import Profile
from .serializers import ProfileSerializer
from drf_api_league_hub.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by("-created_at")


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by("-created_at")
