from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def load_test(request):
    return render(request, 'load_test.html')

def load_test_server(request):
    return render(request, 'load_test_server.html')


def jquery_get(request):
    return render(request, 'jquery_get.html')

def jquery_get_server(request):
    uname  = request.GET.get('uname','no')
    age = request.GET.get('age','no')
    d = {'uname':uname,'age':age}
    return HttpResponse(json.dumps(d),content_type='application/json')


def jquery_post(request):
    return render(request, 'jquery_post.html')

def jquery_post_server(request):
    if int(request.POST.get('age',0)) > 100:
        d = {'msg':'post is too big', 'code':1201}
    else:
        d = {'msg': 'post is OK', 'code': 1201}

    return HttpResponse(json.dumps(d), content_type='application/json')

def jquery_ajax(request):
    return  render(request, 'jquery_ajax.html')

def jquery_ajax_server(request):
    import time
    time.sleep(3)
    d = {'name':'guoxiaonao', 'age':18}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax_user(request):

    return render(request, 'jquery_ajax_user.html')

def jquery_ajax_user_server(request):

    d = [{'name':'guoxiaonao','age':18},{'name':'guoxiaonao2','age':28}]
    return HttpResponse(json.dumps(d), content_type='application/json')


def cross(request):

    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    return HttpResponse(func + "('我出来了')")

def cross_server_json(request):
    func = request.GET.get('callback')
    d = {'name':'guoxiaonao', 'age':18}
    return HttpResponse(func + "(" + json.dumps(d) + ")")







