from django.db import models
from django.forms import ModelForm
from core.models import *
from django.db.models import Avg

class InternetResourceType(models.Model):
	name = models.TextField()
	def __str__(self):
		return self.name

class InternetResource(models.Model):
	url = models.URLField()
	name = models.TextField()
	description = models.TextField()
	resourceType = models.ForeignKey(InternetResourceType)

	datetime = models.DateTimeField(auto_now=True)
	hashdata = models.TextField()

	@property
	def quality(self):
		return self.evaluations.all().aggregate(Avg('value'))['value__avg']
	@property
	def quality_array(self):
		ret = []
		for v in range(int(self.quality)):
			ret.append('*')
		for v in range(int(10-self.quality)):
			ret.append("_")
		return ret


class InternetResourceForm(ModelForm):
	class Meta:
		model = InternetResource
		exclude=["hashdata", "datetime"]
		widgets = {
		}

class Evaluation(models.Model):
	umarell = models.ForeignKey(Umarell, related_name="evaluations")
	resource = models.ForeignKey(InternetResource, related_name="evaluations")
	comment = models.TextField(null=True, blank=True)
	datetime = models.DateTimeField(auto_now=True)
	value = models.IntegerField()

	@property
	def value_array(self):
		ret = []
		for v in range(self.value):
			ret.append('*')
		for v in range(10-self.value):
			ret.append("_")
		return ret

class EvaluationForm(ModelForm):
	class Meta:
		model = Evaluation
		exclude=["umarell", "resource"]