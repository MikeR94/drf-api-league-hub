from rest_framework import serializers
from champions.models import Champion


class ChampionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Champion
        fields = [
            "id",
            "owner",
            "is_owner",
            "created_at",
            "updated_at",
            "name",
            "alias",
            "champ_image",
            "lore",
            "role",
            "champ_class",
            "range",
            "difficulty",
            "passive_ability",
            "passive_ability_description",
            "passive_ability_image",
            "ability_1",
            "ability_1_description",
            "ability_1_image",
            "ability_2",
            "ability_2_description",
            "ability_2_image",
            "ability_3",
            "ability_3_description",
            "ability_3_image",
            "ultimate_ability",
            "ultimate_ability_description",
            "ultimate_ability_image",
        ]
