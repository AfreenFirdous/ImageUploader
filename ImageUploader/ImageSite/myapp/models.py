from django.db import models


class Image(models.Model):
    picture = models.FileField(upload_to='myapp')
    date = models.DateTimeField(auto_now=True)
