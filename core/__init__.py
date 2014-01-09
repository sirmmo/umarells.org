def UmarellsMiddleware(request):
	request.user.is_authenticated()
	return {
	    "user": request.user,
	}