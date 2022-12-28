from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="owner.username")

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
            "is_staff",
            "avatar_image",
        ]
