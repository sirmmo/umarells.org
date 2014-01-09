from django.shortcuts import render_to_response



def signup(request):
	return render_to_response('login.html',{
			"user":request.user if request.user.is_authenticated() else None
		})