from rest_framework import generics, permissions
from drf_api_league_hub.permissions import IsOwnerOrReadOnly
from upvotes.models import UpVote
from upvotes.serializers import UpVoteSerializer


class UpVoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UpVoteSerializer
    queryset = UpVote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpVoteDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = UpVoteSerializer
    queryset = UpVote.objects.all()
