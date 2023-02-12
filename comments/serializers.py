from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer to convert the model into JSON
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(source="owner.profile.avatar_image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    is_staff = serializers.ReadOnlyField(source="owner.profile.is_staff")

    def get_is_owner(self, obj):
        """
        Method to check if the user is the owner
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Method to return the created_at value in a
        more user friendly format
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Method to return the updated_at value in a
        more user friendly format
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_avatar",
            "champion",
            "created_at",
            "updated_at",
            "comment",
            "is_staff",
        ]


class CommentDetailSerializer(CommentSerializer):
    champion = serializers.ReadOnlyField(source="owner.champion.name")
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(source="owner.profile.avatar_image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    is_staff = serializers.ReadOnlyField(source="owner.profile.is_staff")

