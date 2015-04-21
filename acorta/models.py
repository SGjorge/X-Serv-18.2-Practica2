from django.db import models

# Create your models here.

class Urls(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return "<a href=" + self.name + ">" + self.name + "</a> : "+ str(self.id) 
