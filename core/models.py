from django.db import models
from django.contrib.auth.models import User

class Umarell(models.Model):
	user = models.ForeignKey(User, unique=True)

class UmarellBadge(models.Model):
	badgeCriteria = models.TextField()
	name = models.TextField()
	image = models.ImageField()

class UmarellAward(models.Model):
	umarell = models.ForeignKey(Umarell)
	badge = models.ForeignKey(UmarellBadge)
	datetime = models.DateTimeField(auto_now=True)