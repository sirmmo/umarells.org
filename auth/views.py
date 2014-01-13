from django.http import HttpResponse
import json
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Token

# Create your views here.

@csrf_exempt
def get_token(request):
	d = json.loads(request.REQUEST.get('data'))
	user = d.get('u')
	password = d.get('p')

	user = authenticate(username=user, password=password)
	if user is not None:
		t, c = Token.objects.get_or_create(user = user)
		if c:
			t.save()
		return HttpResponse(json.dumps({"token":t.uuid}))
	else:
		return HttpResponse(json.dumps({"token":""}))

@csrf_exempt
def verify_token(request):
	d = json.loads(request.REQUEST.get('data'))
	token = d.get('t')

	try:
		Token.objects.get(uuid = token)
		return HttpResonse(json.dumps(True))
	except:
		return HttpResonse(json.dumps(False))

class TokenMiddleware(object):
	def process_request(self, request):
		try:
			a = request.user
		except:
			try:
				request.user = Token.objects.get(uuid=request.REQUEST.get('t')).user
			except:
				pass

