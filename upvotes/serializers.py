from rest_framework import serializers
from upvotes.models import UpVote
from django.db import IntegrityError


class UpVoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    champion_name = serializers.ReadOnlyField(source="champion.name")

    class Meta:
        model = UpVote
        fields = [
            "id",
            "owner",
            "champion_name",
            "created_at",
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "Possible duplicate vote!"})
