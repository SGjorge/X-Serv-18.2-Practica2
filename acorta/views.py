from django.shortcuts import render
from django.conf.urls import patterns, include, url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest,\
HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from models import Urls

# Create your views here.

def getform():
	form = "<form action='' method='POST'>\n"
	form += "Page: <input type='text' name='name' value=''><br>\n"
	form += "<input type='submit' value='enviar'>\n"
	form += "</form>\n"
	return form

def getUrls(urlList):
    urls = ""
    for url in urlList:
        urls += str(url) + "<br/>"
    return urls

def redirect(request,resourceName):
    try:
        url = Urls.objects.get(id=resourceName)
    except Urls.DoesNotExist:
        return HttpResponseNotFound(str(resourceName) + " not found")
    return HttpResponseRedirect(url.name)

@csrf_exempt
def acorta(request,resourceName):
    response = "welcome to urlshort" + "<br/>"
    urlsList = Urls.objects.all()
    response += getUrls(urlsList) + "<br/>"
    if request.method == 'POST':
        if request.POST['name'] == "":
            return HttpResponseBadRequest("EMPTY POST")
        elif not request.POST['name'].startswith("http://") and not request.POST['name'].startswith("https://"):
            page = "http://" + request.POST['name']
        newUrl = Urls(name=page)
        newUrl.save()
        response += "--Page: <a href=" + request.POST['name'] + ">" + request.POST['name'] + "</a></p>\n"
        response += "-- Url short: <a href=" + str(newUrl.id) + ">" +  str(newUrl.id) + "</a></p>" 
    elif request.method == 'GET':
        try:
            content = Urls.objects.get(name=resourceName)
            response += content.name
        except Urls.DoesNotExist:
            response += getform()
    return HttpResponse(response)

