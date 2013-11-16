from django.db import models
from core.models import *

class InternetResourceType(models.Model):
	name = models.TextField()

class InternetResource(models.Model):
	url = models.URLField()
	description = models.TextField()
	resourceType = models.ForeignKey(InternetResourceType)
	hashdata = models.TextField()

class Evaluation(models.Model):
	umarell = models.ForeignKey(Umarell)
	resource = models.ForeignKey(InternetResource)
	comment = models.TextField(null=True, blank=True)
	value = models.IntegerField(min_value = 1)