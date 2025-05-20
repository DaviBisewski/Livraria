from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='images/')
