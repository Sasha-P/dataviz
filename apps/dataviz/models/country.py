from django.db import models

from .region import Region


class Country(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=100, unique=True)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
