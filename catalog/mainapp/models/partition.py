from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from .good import Good
from django.contrib.sites.models import Site


class Partition(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    goods = models.ManyToManyField(Good, related_name='partitions')
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()
