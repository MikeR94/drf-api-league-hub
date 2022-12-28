from rest_framework import generics
from profiles.models import Profile
from .serializers import ProfileSerializer
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by("-created_at")
