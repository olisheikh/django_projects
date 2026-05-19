from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_images = models.ImageField(upload_to='images/')
    post_files = models.FileField(upload_to='files/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    


