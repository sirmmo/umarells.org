from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import *
def profile(request, username=None):
	return render_to_response('profile.html',{
			"edit":username == request.user.username, 
			"user":request.user if username is None and request.user.is_authenticated() else User.objects.get(username=username)
		}
	)

def index(request):

	if 'labs.it' in request.META.get('HTTP_HOST'):
		return HttpResponseRedirect('/cityfix')
		
	return render_to_response('index.html',{
			"user":request.user if request.user.is_authenticated() else None,
			'umarells':Umarell.objects.order_by('?')[0:8]
		})