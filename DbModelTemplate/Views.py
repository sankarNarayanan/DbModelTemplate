from django.contrib import postgres
import json
from django.shortcuts import HttpResponse
import json
from django.template import loader


def index(request):
    data = {}
    json_data = {}

    responseString = "{\"nodes\" : [{\"id\":\"id1\",\"text\":\"text1\"},{\"id\":\"id2\",\"text\":\"text2\"}]}"

    if request.method == "POST":
        data['request'] = 'request is POST'
        json_data = json.dumps(data)
    else:
        print request.method
        json_data = json.dumps(data)
    return HttpResponse(json_data)
