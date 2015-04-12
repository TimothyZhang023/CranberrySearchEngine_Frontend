# Create your views here.
import random
import urllib
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import requests, json
from CSE_Frontend import settings


def urlencode(str):
    reprStr = repr(str).replace(r'\x', '%')
    return reprStr[1:-1]


def _get_index_api():
    servers = settings.CSE_BACKEND_ENDPOINT
    random.shuffle(servers)
    return servers[0]


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def query(request, key):
    p = request.GET.get('p', '1')
    url = _get_index_api() + urllib.quote(key.encode("utf-8").replace("\\", "%2f"))
    params = {"p": p, }
    r = requests.get(url, params=params)
    print r.url, r.status_code
    if r.status_code == 200:
        json_res = r.json()

        keyWord = json_res['keyWord'].replace("%2f", "\\")
        pager = json_res['pager']
        queryResultItems = json_res['queryResultItems']
        timeSpeed = json_res['timeSpeed'] / 1000.0

        empty_counter = range(1, pager['totalPage'])
        #print json_res

        return render_to_response('query.html', {'keyWord': keyWord, 'pager': pager, 'empty_counter': empty_counter,
                                                 'timeSpeed': timeSpeed,
                                                 'queryResultItems': queryResultItems},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponse("error")


def q(request):
    if request.method == 'POST':
        key = request.POST['keyWords']

        return HttpResponseRedirect(reverse('query', args={key}))
    return HttpResponse("error visit method")
