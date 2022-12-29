from rest_framework import generics, permissions
from drf_api_league_hub.permissions import IsOwnerOrReadOnly
from comments.models import Comment
from comments.serializers import (
    CommentSerializer,
    CommentDetailSerializer,
    CommentDeleteSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "champion",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


class CommentDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CommentDeleteSerializer
    queryset = Comment.objects.all()
