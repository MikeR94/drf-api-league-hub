from django.db import models
from django.contrib.auth.models import User
from champions.models import Champion


class Comment(models.Model):
    """
    Comment model, related to User and Champion
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.comment
