from django.db import models
from .good import Good


class Partition(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    goods = models.ManyToManyField(Good, related_name='partitions')
