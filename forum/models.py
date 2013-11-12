from django.db import models
from umarells.core.models import *

class Thread(models.Model):
	title = models.TextField()
	author = models.ForeignKey(Umarell)
	date = models.DateTimeField(auto_now=True)

class ThreadResponse(Thread):
	thread = models.ForeignKey(Thread)