from rest_framework import generics, permissions
from drf_api_league_hub.permissions import IsOwnerOrReadOnly, IsStaffOrOwnerOrReadOnly
from comments.models import Comment
from comments.serializers import (
    CommentSerializer,
    CommentDetailSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    """
    List all comments and allow users to create a comment
    if they have an account
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "champion",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a comment and allow the comment owner to
    update the comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


class CommentDelete(generics.RetrieveDestroyAPIView):
    """
    Allow a comment to be deleted if the user is a staff
    member or the comment owner
    """
    permission_classes = [IsStaffOrOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
