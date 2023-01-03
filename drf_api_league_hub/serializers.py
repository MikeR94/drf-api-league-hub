from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_avatar = serializers.ReadOnlyField(source="profile.avatar_image.url")
    is_staff = serializers.ReadOnlyField(source="profile.is_staff")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id",
            "profile_avatar",
            "is_staff",
        )
