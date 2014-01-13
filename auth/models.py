from django.db import models

from uuid import uuid4
from django.contrib.auth.models import User

def get_uuid():
	return str(uuid4())

class Token(models.Model):
	user = models.ForeignKey(User)
	uuid = models.TextField(default=get_uuid)

	def __str__(self):
		return self.uuid
