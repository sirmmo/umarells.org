from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt 

from datetime import datetime

import uuid

from .models import *

import json

def index(request):
	return render_to_response('map.html',{"user":request.user if request.user.is_authenticated() else None,})

def map(request):
	geoj = { 
		"type": "FeatureCollection",
		"features": [{ 
			"type": "Feature",
			"geometry": {
				"type": "Point", 
				"coordinates": [cf.lon, cf.lat]
			},
			"properties": {
				"note":cf.description,
				"fixtype":str(cf.fixtype),
				"sitetype":str(cf.sitetype),
				"operator":str(cf.operator),
				"infrastructure":str(cf.infrastructure),
				"images":[pic.url() for pic in cf.pics.all()]

			}
		} for cf in CityFix.objects.all()]
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
	cf = CityFix()
	cf.lon = meta.get('position')[0]
	cf.lat = meta.get('position')[1]
	cf.sent = datetime.utcfromtimestamp(meta.get('timestamp')/1000)

	cf.description = form.get('note')
	cf.fixtype = FixType.objects.get(id=int(form.get('type'))+1)
	cf.sitetype = SiteType.objects.get(id=int(form.get('sitetype'))+1)
	cf.operator = Operator.objects.get(id=int(form.get('operator'))+1)
	cf.infrastructure = Infrastructure.objects.get(id=int(form.get('infrastructure'))+1)
	cf.save()

	return HttpResponse(json.dumps({"success":True, "uuid":str(cf.uuid)}))

from django.core.files.images import ImageFile
import base64

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
	return render_to_response('labswatch_meta.json')

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
	res['Content-Disposition'] = 'attachment; filename=' + os.path.basename(pic)    

