from rest_framework import serializers
from upvotes.models import UpVote
from django.db import IntegrityError


class UpVoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = UpVote
        fields = [
            "id",
            "owner",
            "champion",
            "created_at",
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "Possible duplicate vote!"})
