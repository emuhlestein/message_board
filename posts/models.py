from django.db import models

class Post(models.Model):
    text = models.TextField()

    # return a string representation of the object
    def __str__(self):
        return self.text