from rest_framework import serializers
from upvotes.models import UpVote
from django.db import IntegrityError


class UpVoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the upvote model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    champion_name = serializers.ReadOnlyField(source="champion.name")

    class Meta:
        model = UpVote
        fields = [
            "id",
            "owner",
            "champion_name",
            "created_at",
            "champion",
        ]

    def create(self, validated_data):
        """
        Create a new upvote if it is unique
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "Possible duplicate vote!"})
