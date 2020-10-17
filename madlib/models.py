from django.db import models


# Create your models here.
class MadlibFields(models.Model):

    def __str__(self):
        return f"Mad lib Fields"

    adjective = models.CharField(max_length=25)
    verb = models.CharField(max_length=25)
    adjective2 = models.CharField(max_length=25)
    adverb = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    animal = models.CharField(max_length=25)


