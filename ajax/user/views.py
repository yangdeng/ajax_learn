from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from user.models import User


def xhr(request):
    return render(request, 'xhr.html')

def get_xhr(request):
    return render(request, 'get-xhr.html')

def get_xhr_server(request):
    if request.GET.get('uname'):
        uname = request.GET['uname']
        return HttpResponse('weclome %s' %uname)
    return HttpResponse('this is ajax request !')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        #注册
        uname = request.POST.get('uname');
        if not uname:
            return HttpResponse('请输入用户名')
        pwd = request.POST.get('pwd')
        if not pwd:
            return HttpResponse('请输入密码')
        nickname = request.POST.get('nickname')
        if not nickname:
            return HttpResponse('请输入昵称')

        try:
            User.objects.create(
                uname=uname, pwd=pwd, nickname=nickname
            )
        except Exception as e:
            return HttpResponse('注册失败，请稍后重试')

        return HttpResponse('注册成功')


def checkuname(request):
    uname = request.GET.get('uname')
    #查看用户名是否存在
    users = User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse('1')
    return HttpResponse('0')

def make_post(request):
    if request.method == 'GET':
        return render(request, 'make_post.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        return HttpResponse('your post is ok')
    else:
        raise


def get_user(request):

    return render(request,'get-user.html')


def get_user_server(request):
    users = User.objects.all()
    msg = ''
    for u in users:
        msg += '%s_%s_%s|' % (u.uname,u.pwd,u.nickname)
    last_msg = msg[0:-1]
    return HttpResponse(last_msg)

def json_obj(request):
    return render(request, 'json_obj.html')

def json_dumps(request):
    #１．生成单个对象的json字符串 序列化-> obj-str
    dic = {
        'uname':'LILI',
        'uage':'30'
    }
    #字符串必须有序时候加sort_keys=True
    #json_str = json.dumps(dic)
    json_str = json.dumps(dic, sort_keys=True,separators=(',',':'))
    #2。生成多个对象的json字符串
    s = [
        {
            'uname': 'LILI',
            'age': 18
        },
        {
            'uname':'panghu',
            'age':20
        }
    ]
    json_str_arr = json.dumps(s)

    from django.core import serializers
    users = User.objects.all()
    json_str_arr = serializers.serialize('json', users)
    #return HttpResponse(json_str_arr,content_type='application/json')


    return JsonResponse({'uname':'guoxiaonao'})




























