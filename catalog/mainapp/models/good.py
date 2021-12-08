from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Good(models.Model):
    name = models.CharField(max_length=128)
    arrived = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])
    quantity = models.PositiveIntegerField()
    supplier_name = models.CharField(max_length=128)
    sites = models.ManyToManyField(Site)
    objects = models.Manager()
    on_site = CurrentSiteManager('sites')
