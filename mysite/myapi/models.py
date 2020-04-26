import os


from django.db import models
from django.conf import settings

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    # image = models.FilePathField(path=os.path.join(settings.STATIC_ROOT, 'myapi'))
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return self.name + " by " + str(self.host)
