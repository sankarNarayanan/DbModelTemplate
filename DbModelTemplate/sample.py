from django.shortcuts import HttpResponse
import json
from django.shortcuts import render_to_response
import os
from django.template import loader
from django.template.context_processors import request
from DbModelTemplate.models import User


def index(request):
    data = {}
    json_data = {}
    
    if request.method == "POST":
        data['request'] = 'request is POST'
        json_data = json.dumps(data)
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render(json_data, request))
        return render_to_response('login.html')
        data['request'] = 'request is GET'
        json_data = json.dumps(data)
    return HttpResponse(json_data)

def createUser(request):
    obj = User.objects.create(userName=request.POST.get('userName'), password= request.POST.get('password'), phoneNumber=request.POST.get('phone'), emailId = request.POST.get('email'))
    obj.save()
    return HttpResponse(request.POST.get('userName'))
