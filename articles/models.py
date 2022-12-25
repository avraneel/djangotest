from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)   # charfield for small amt of text
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #author
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50]+"..."