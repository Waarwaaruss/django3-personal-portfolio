from django.db import models

class  Gallery(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='gallery/images')
    
    def __str__(self):
        return self.title