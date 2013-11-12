from django.db import models
from umarells.core.models import *


class Element(models.Model):
	topics = models.ManyToManyField(Topic)
	types = models.ManyToManyField(Type)
	name = models.TextField()
	url = models.URLField(null=True, blank=True)

	class Meta:
		abstract=True

class App(Element):
	pass

class Service(Element):
	pass