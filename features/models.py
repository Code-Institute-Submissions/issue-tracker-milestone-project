from django.db import models

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()


    def __str__(self):
        return self.name
