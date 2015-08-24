from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt 

from datetime import datetime

import uuid

from .models import *
from auth.models import *



from pytz import timezone
import pytz

import json

def index(request):
	dynamic_base = "base.html"
	if 'labs.it' in request.META.get('HTTP_HOST'):
		dynamic_base = "citywatch_base.html"
	return render_to_response('map.html',{"dynamic_base":dynamic_base, "user":request.user if request.user.is_authenticated() else None,})


def map(request):
	bbox = json.loads("[%s]" % request.REQUEST.get('bbox', "-90,-180,90,180"))
	f = {
		"lon__gte": bbox[0],
		"lat__gte": bbox[1],
		"lon__lte": bbox[2],
		"lat__lte": bbox[3],
	}
	geoj = { 
		"type": "FeatureCollection",
		"features": [{ 
			"type": "Feature",
			"geometry": {
				"type": "Point", 
				"coordinates": [cf.lon, cf.lat]
			},
			"properties": {
				"ID":cf.id,
				"Nota":cf.description,
				"Utente":cf.user.username if cf.user is not None else "",
				"Tipo di problematica":str(cf.fixtype),
				"Tipo di collocazione":str(cf.sitetype),
				"Operatore":str(cf.operator),
				"Infrastruttura":str(cf.infrastructure),
				"images":[pic.url() for pic in cf.pics.all()],
				"Data":cf.sent.astimezone(timezone("Europe/Rome")).strftime("%d/%m/%Y %H:%M")

			}
		} for cf in CityFix.objects.filter(**f)]
	} 
	return HttpResponse(json.dumps(geoj))
'''

{
	"form":{"type":"1","sitetype":"0","infrastructure":"1","note":"","operator":"1"},
	"meta":{"timestamp":1389182454933,"position":[11.2699404,44.4301183],"has_attach":true}
}

'''
@csrf_exempt
def push(request):
	data = json.loads(request.REQUEST.get('data'))
	form = data.get('form')
	meta = data.get('meta')

	tok = request.REQUEST.get('token')

	user = Token.objects.get(uuid = tok).user

	cf = CityFix()
	cf.lon = meta.get('position')[0]
	cf.lat = meta.get('position')[1]
	cf.sent = datetime.utcfromtimestamp(meta.get('timestamp')/1000)
	cf.user = user
	cf.description = form.get('note')
	cf.fixtype = FixType.objects.get(id=int(form.get('type')))
	cf.sitetype = SiteType.objects.get(id=int(form.get('sitetype')))
	cf.operator = Operator.objects.get(id=int(form.get('operator')))
	cf.infrastructure = Infrastructure.objects.get(id=int(form.get('infrastructure')))

	cf.save()

	return HttpResponse(json.dumps({"success":True, "uuid":str(cf.uuid)}))


def app(request):
	import os.path
	import mimetypes
	mimetypes.init()


	file_path = "/var/www/umarells/app/CityWatch.apk"
	fsock = open(file_path,"r")
	file_name = os.path.basename(file_path)
	file_size = os.path.getsize(file_path)
	print "file size is: " + str(file_size)
	mime_type_guess = mimetypes.guess_type(file_name)
	
	response = HttpResponse(fsock, mimetype=mime_type_guess[0])
	response['Content-Disposition'] = 'attachment; filename=' + file_name            
	return response 

from django.core.files.images import ImageFile
import base64
import os
@csrf_exempt
def push_file(request, uuid):
	if request.REQUEST.get('data') is not None :
		return HttpResponse(json.dumps({"success":True}))
	p = Pics()
	p.fix = CityFix.objects.get(uuid=uuid)
	p.save()

	the_id = p.id
	g = open("/tmp/%s-%s.jpg" % (uuid, the_id), "w")
	#print request.REQUEST.get('file')
	#print base64.decodestring(request.REQUEST.get('file'))
	g.write(base64.decodestring(request.REQUEST.get('file')))
	g.close()
	
	p.pic = "/tmp/%s-%s.jpg" % (uuid, the_id)
	p.save()
	
	return HttpResponse(json.dumps({"success":True, "uuid":uuid, "uploaded":p.pic is not None}))

def form(request):
	return render_to_response("labswatch.json")

def form_meta(request):
	ret = {}

	ret["fields"] = {}
	ret["title"] = "Segnalazione"
	ret["fields"] = {
		"infrastructure":{
			"options":{i.id:i.name for i in Infrastructure.objects.all()},
			"sort":["1","2","3","4"],
       		"title": "Infrastruttura"
			},
		"note":{
            "description": "Caratteristiche dell'anomalia.",
            "title": "Descrizione"
		},
		"operator":{
       		"description": "Ente responsabile dell'installazione.",
			"options":{i.id:i.name for i in Operator.objects.all()},
			"sort":["1","2","3","4","5","6","7","8","9"],
        	"title": "Operatore"
		},
		"sitetype":{
			"options":{i.id:i.name for i in SiteType.objects.all()},
			"sort":["1","2"],
        	"title": "Sede"
		},
		"type":{
			"options":{i.id:i.name for i in FixType.objects.all()},
			"sort":["2","1"],
        	"title": "Tipologia"
		},
	}
	ret["form_sort"] = [
				        "type",
				        "infrastructure",
				        "sitetype",
				        "operator",
				        "note"
				    ]
	return HttpResponse(json.dumps(ret))

def image(request, uuid, id):
	import mimetypes
	print "qwe"
	mimetypes.init()
	print "rty"
	pic = Pics.objects.get(id=id).pic
	print "uio"
	f = open(pic, "r")
	mime = mimetypes.guess_type(pic)
	res = HttpResponse(f, mimetype = mime[0])   
	return res

