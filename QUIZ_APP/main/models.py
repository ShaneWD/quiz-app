from django.db import models
from users.models import User


class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    data = models.JSONField()

    created = models.DateTimeField( auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)