from django.shortcuts import render, HttpResponse

# Create your views here.
# .表示当前包下的models
import json
from main.models import message
from django.core.paginator import Paginator
from datetime import datetime
from django.http import JsonResponse


# class sub(View):
#    def get(self, request):
#        metro.objects.create(trains='南京地铁10号线', date='2020-02-10', carriage='', depstation='龙华路站',
#                             arrstation='临江站', addinf='', starttime='2020-02-10 上午7:50:00', endtime='2020-02-10 下午11:59:59',
#                             source='北京交通广播',subtime='2020-02-21 下午1:10:40')
#        return HttpResponse('submit successfully')
# def index(request):
#    return HttpResponse('QuerySystem.html')

def index(request):
    return render(request, '../templates/QueryWeb.html')

def post_message(request):

    message_post = message.objects.all()
    dataCount = message_post.count()
    list = []
    for i in message_post:
        dict = {}
        dict['t_type'] = i.t_type
        dict['t_no'] = i.t_no
        dict['t_date'] = i.t_date
        dict['t_no_sub'] = i.t_no_sub
        dict['t_pos_start'] = i.t_pos_start
        dict['t_pos_end'] = i.t_pos_end
        dict['t_memo'] = i.t_memo
        dict['t_start'] = i.t_start
        dict['t_end'] = i.t_end
        dict['source'] = i.source
        dict['who'] = i.who
        dict['created_at'] = i.created_at
        dict['updated_at'] = i.updated_at
        dict['verified'] = i.verified
        list.append(dict)
    Result = {"code": 0, "msg": "", "count": dataCount, "data": list}
    return JsonResponse(Result)
