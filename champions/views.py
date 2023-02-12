from rest_framework import generics, filters
from champions.models import Champion
from champions.serializers import ChampionSerializer
from drf_api_league_hub.permissions import IsStaffOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ChampionList(generics.ListAPIView):
    """
    Return a list of all champions ordered by name
    with additional search and filter functionality
    """
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("name")
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["role"]


class ChampionDetail(generics.RetrieveAPIView):
    """
    Retrieves and returns a champion 
    ordered by creation date
    """
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")


class ChampionEdit(generics.RetrieveUpdateAPIView):
    """
    Allows staff members only to retrieve and update
    a champion
    """
    permission_classes = [
        IsStaffOrReadOnly,
    ]
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")


class ChampionDelete(generics.RetrieveDestroyAPIView):
    """
    Allows staff members only to retrieve and delete
    a champion
    """
    permission_classes = [
        IsStaffOrReadOnly,
    ]
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")


class ChampionCreate(generics.ListCreateAPIView):
    """
    Allows staff members only to create a champion
    """
    permission_classes = [
        IsStaffOrReadOnly,
    ]
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChampionLeaderboard(generics.ListAPIView):
    """
    Returns a list of champions ordered by upvotes
    """
    serializer_class = ChampionSerializer
    queryset = Champion.objects.annotate(
        upvotes_count=Count("upvotes", distinct=True)
    ).order_by("-upvotes_count")
