from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	name = models.TextField()

class Type(models.Model):
	name = models.TextField()

class Umarell(models.Model):
	user = models.ForeignKey(User, unique=True)
	interests = models.ManyToManyField(Topic)

class UmarellBadge(models.Model):
	badgeCriteria = models.TextField()
	name = models.TextField()
	image = models.ImageField(upload_to="/tmp")

class UmarellAward(models.Model):
	umarell = models.ForeignKey(Umarell)
	badge = models.ForeignKey(UmarellBadge)
	datetime = models.DateTimeField(auto_now=True)