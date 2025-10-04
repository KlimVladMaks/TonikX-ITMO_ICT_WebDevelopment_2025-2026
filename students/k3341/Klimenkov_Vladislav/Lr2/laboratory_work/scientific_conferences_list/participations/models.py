from django.db import models
from users.models import User
from conferences.models import Conference


class Presentation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.topic} — {self.author}"
