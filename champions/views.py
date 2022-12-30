from rest_framework import generics, permissions, filters
from champions.models import Champion
from champions.serializers import ChampionSerializer
from drf_api_league_hub.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ChampionList(generics.ListAPIView):
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["role"]


class ChampionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")


class ChampionCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
