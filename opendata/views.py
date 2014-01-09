from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import *
def index(request):
	return render_to_response('opendata.html',{
			"user":request.user if request.user.is_authenticated() else None,
			"datasets":InternetResource.objects.all()
		})

@login_required
@csrf_exempt 
def add_internet_resource(request):
	if request.method == 'POST':
		form = InternetResourceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/opendata')
	else:
		form = InternetResourceForm()
	return render_to_response("form.html", {
		"user":request.user if request.user.is_authenticated() else None,
		"form": form,
	})

def remove_interet_resource(request):
	pass

@login_required
@csrf_exempt 
def evaluate_internet_resource(request):
	if request.method == 'POST':
		form = EvaluationForm(request.POST, request.FILES)
		if form.is_valid():
			ev = form.save(commit=False)
			ev.umarell = Umarell.objects.get(user = request.user)
			ev.resource = InternetResource.objects.get(id=request.REQUEST.get('resource'))
			ev.save()
			
			return HttpResponseRedirect('/opendata')
	else:
		form = EvaluationForm()
	return render_to_response("form.html", {
		"user":request.user if request.user.is_authenticated() else None,
		"form": form,
	})

def show_resource(request, resource):
	r = InternetResource.objects.get(id=resource)
	return render_to_response("resource.html", {
				"user":request.user if request.user.is_authenticated() else None,
"dataset":r})