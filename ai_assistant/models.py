from django.db import models
from django.contrib.auth.models import User

class ChatLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
