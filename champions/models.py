from django.db import models
from django.contrib.auth.models import User


class Champion(models.Model):
    """
    Champion model
    """

    role_choices = [
        ("top", "Top"),
        ("mid", "Mid"),
        ("jungle", "Jungle"),
        ("adc", "ADC"),
        ("support", "Support"),
    ]

    champ_class_choices = [
        ("controller", "Controller"),
        ("fighter", "Fighter"),
        ("mage", "Mage"),
        ("marksman", "Marksman"),
        ("slayer", "Slayer"),
        ("tank", "Tank"),
        ("specialist", "Specialist"),
    ]

    range_choices = [
        ("melee", "Melee"),
        ("ranged", "Ranged"),
    ]

    difficulty_choices = [
        ("low", "Low"),
        ("moderate", "Moderate"),
        ("high", "High"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    champ_image = models.ImageField(
        upload_to="images/", default="../Ivern_0_iumwtm", blank=False
    )
    lore = models.TextField(blank=False)
    role = models.CharField(
        max_length=32, choices=role_choices, default="top", blank=False
    )
    champ_class = models.CharField(
        max_length=32, choices=champ_class_choices, default="controller", blank=False
    )
    range = models.CharField(
        max_length=32, choices=range_choices, default="melee", blank=False
    )
    difficulty = models.CharField(
        max_length=32, choices=difficulty_choices, default="low", blank=False
    )
    passive_ability = models.CharField(max_length=255)
    passive_ability_description = models.TextField(blank=False)
    passive_ability_image = models.ImageField(
        upload_to="images/", default="../IvernW_muxhxj", blank=False
    )
    ability_1 = models.CharField(max_length=255)
    ability_1_description = models.TextField(blank=False)
    ability_1_image = models.ImageField(
        upload_to="images/", default="../IvernW_muxhxj", blank=False
    )
    ability_2 = models.CharField(max_length=255)
    ability_2_description = models.TextField(blank=False)
    ability_2_image = models.ImageField(
        upload_to="images/", default="../IvernW_muxhxj", blank=False
    )
    ability_3 = models.CharField(max_length=255)
    ability_3_description = models.TextField(blank=False)
    ability_3_image = models.ImageField(
        upload_to="images/", default="../IvernW_muxhxj", blank=False
    )
    ultimate_ability = models.CharField(max_length=255)
    ultimate_ability_description = models.TextField(blank=False)
    ultimate_ability_image = models.ImageField(
        upload_to="images/", default="../IvernW_muxhxj", blank=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.name}"
