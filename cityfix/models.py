from django.db import models
from core.models import *

from django.core.urlresolvers import reverse

from uuid import uuid4
def get_uuid():
	return str(uuid4())

class FixType(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name

class Operator(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name

class Infrastructure(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name

class SiteType(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name


class CityFix(models.Model):
	uuid = models.TextField(default=get_uuid, editable=False, unique=True)
	lon = models.FloatField()
	lat = models.FloatField()

	

	umarell = models.ForeignKey(Umarell, null=True)
	description = models.TextField(null=True, blank=True)
	fixtype = models.ForeignKey(FixType)
	sitetype = models.ForeignKey(SiteType)
	operator = models.ForeignKey(Operator)
	infrastructure = models.ForeignKey(Infrastructure)
	sent = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description

class Pics(models.Model):
	fix = models.ForeignKey(CityFix, related_name="pics")
	pic = models.TextField(null=True)

	def __str__(self):
		return self.pic

	def url(self):
		return reverse('cityfix_img', kwargs={"uuid":self.fix.uuid, "id":self.id})


