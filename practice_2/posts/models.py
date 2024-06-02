from django.db import models
from author.models import Author

# Create your models here.
class Post(models.Model):
    album_name = models.CharField(max_length=100)
    album_release_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    musician = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.album_name