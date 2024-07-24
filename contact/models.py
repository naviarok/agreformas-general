from django.db import models
import uuid

class Message(models.Model):
    fullname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)
    message = models.TextField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    def __str__(self) -> str:
        return self.fullname