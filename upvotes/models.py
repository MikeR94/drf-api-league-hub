from django.db import models
from django.contrib.auth.models import User
from champions.models import Champion


class UpVote(models.Model):
    """
    Upvote model, related to User and Champion
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    champion = models.ForeignKey(
        Champion, on_delete=models.CASCADE, related_name="upvotes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "champion"]

    def __str__(self):
        return f"{self.owner} {self.champion}"
