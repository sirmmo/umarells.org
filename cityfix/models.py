from django.db import models
from core.models import *

class FixType(models.Model):
	name = models.TextField()

class CityFix(models.Model):
	lon = models.FloatField()
	lat = models.FloatField()

	umarell = models.ForeignKey(Umarell)
	pic = models.ImageField(null=True, blank=True)

	description = models.TextField(null=True, blank=True)

	fixtype = models.ForeignKey(FixType)