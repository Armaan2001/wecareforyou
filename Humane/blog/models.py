from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)


def __str__(self):
    return self.title