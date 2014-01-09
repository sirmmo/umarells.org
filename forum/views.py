from django.shortcuts import render_to_response

def index(request):
	return render_to_response('opendata.html',{
			"user":request.user if request.user.is_authenticated() else None
		})