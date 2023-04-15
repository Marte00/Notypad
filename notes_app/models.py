from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Folder(models.Model):
    title = models.CharField(max_length=255)

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('title','content')

