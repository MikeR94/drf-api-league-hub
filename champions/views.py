from rest_framework import generics, permissions
from champions.models import Champion
from champions.serializers import ChampionSerializer
from drf_api_league_hub.permissions import IsOwnerOrReadOnly


class ChampionList(generics.ListAPIView):
    serializer_class = ChampionSerializer
    queryset = Champion.objects.all().order_by("-created_at")


class ChampionDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChampionSerializer
    queryset = Champion.objects.all().order_by("-created_at")
