from django.db import models

# Create your models here.
class Mention(models.Model):
    platform = models.CharField(max_length=50)
    content = models.TextField()
    sentiment = models.CharField(max_length=10)  
    topic = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform}: {self.content[:50]}"