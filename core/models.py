from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	name = models.TextField()

class Type(models.Model):
	name = models.TextField()

class Info(models.Model):
	name = models.TextField()
	itype = models.TextField()

class Umarell(models.Model):
	user = models.ForeignKey(User, unique=True, related_name="profile")
	interests = models.ManyToManyField(Topic, null=True, blank=True)

	def __str__(self):
		return self.user.username

class UmarellInfo(models.Model):
	user = models.ForeignKey(Umarell, related_name='infos')
	info = models.ForeignKey(Info)
	value = models.TextField()

class UmarellBadge(models.Model):
	badgeCriteria = models.TextField()
	name = models.TextField()
	image = models.ImageField(upload_to="/tmp")

class UmarellAward(models.Model):
	umarell = models.ForeignKey(Umarell, related_name='awards')
	badge = models.ForeignKey(UmarellBadge)
	datetime = models.DateTimeField(auto_now=True)


from django.db.models.signals import post_save
def create_profile(sender, **kw):
	user = kw["instance"]
	if kw["created"] or Umarell.objects.filter(user = user).count() == 1 :
		profile = Umarell()
		profile.user = user
		profile.save()