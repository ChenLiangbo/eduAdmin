# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.db import connection
from models import *
from django.db.models import Avg, Max, Min, Count, Q
from django.contrib.admin.models import LogEntry
from django.views.decorators.csrf import csrf_exempt
import time, datetime, re, os
from django.contrib.auth.decorators import login_required
try:
    import json
except:
    import simplejson as json  
from django.http import HttpResponse  


#Transform data to json and response to app request
def response_with_json(data,method):
    jsondata  = json.dumps(data,separators = (',',':'))
    response  = HttpResponse('%s' % (jsondata))
    response['Access-Control-Allow-Origin']= "*"
    response['Access-Control-Allow-Methods'] = method 
    response['Access-Control-Allow-Headers'] = "x-requested-with,content-type" 
    return response


@csrf_exempt
def userLogin(request):
    print("============running in login============")
    if request.method == 'GET':
        for key in request.GET:
            print("key = %s,value = %s" % (key,request.GET[key]))
        try:
            user = request.GET.get("username")
            pswd = request.GET.get("password")
        except Exception as e:
            print("Exceprion:",str(e))
            return response_with_json({"code":200,"msg":str(e),"flag":"fail"},request.method)      
        users  = User.objects.filter(username = user)
        if len(users) > 0:
            flag = users[0].check_password(pswd)
            if flag ==  True:
                ret = "success"
                user0 = authenticate(username=user, password=pswd)  #nessary for check user
                login(request, user0)
                token = users[0].id
                message = u"欢迎登录系统！"
            else:
                ret = "fail"
                token = ''
                message =  u"对不起，你输入的密码有错，请重新输入。。。"
        else:
            ret = "fail"
            token = ''
            message = u"对不起，你输入的用户名有错，请重新输入。。。"
        data = {}
        data["flag"] = ret
        data['msg']  = message
        data["code"] = 200
        #print("return okay!")
        return response_with_json(data,request.method)


    elif request.method == 'POST': 
        data = {}    
        try:
            body_str = request.body
            body_dict = json.loads(body_str)
            user = body_dict['username']
            pswd = body_dict['password']
            print(user,pswd)
        except:
            response  = response_with_json(data,request.method)
            return response        
        users  = User.objects.filter(username = user)
        if len(users) > 0:         
            flag = users[0].check_password(pswd)
            if flag ==  True:
                ret = "success"
                user0 = authenticate(username=user, password=pswd)  #nessary for check user
                login(request, user0)
                token = users[0].id
                message = u"欢迎登录系统！"
            else:                
                ret = "fail"
                token = ''
                message =  u"对不起，你输入的密码有错，请重新输入。。。"
        else:
            ret = "fail"
            token = ''
            message = u"对不起，你输入的用户名有错，请重新输入。。。"
        data["flag"] = ret
        data['msg']  = message
        data["code"] = 200
        return response_with_json(data,request.method)


def getLesson(request):
    print("running in getLesson")
    if request.method == 'GET': 
        for key in request.GET:
            print key,request.GET[key]
        try:        
            lessonName = request.GET.get("name") 
        except:
            response  = response_with_json({},request.method)
            return response #response nothing but without any server bug

        lessonObjects = Lesson.objects.filter(name = lessonName)
        if len(lessonObjects) == 0:
            return response_with_json({},request.method)
        data = []
        for lobject in lessonObjects:
            tdict = {}
            tdict['id']        = lobject.id
            tdict['name']      = lobject.name
            tdict['lessonID']  = lobject.lessonID
            tdict['teacher']   = lobject.teacher.name
            tdict['listener']  = lobject.listener
            tdict['place']     = lobject.place
            tdict['season']    = lobject.season
            #tdict['ltime']     = lobject.ltime
            tdict['note']      = lobject.note
            data.append(tdict)
        return response_with_json(data,request.method)

    else:
        return response_with_json("post method is not servered",request.method)
