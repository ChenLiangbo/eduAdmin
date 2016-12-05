# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from models import *
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.views.edit import CreateAdminView,UpdateAdminView
from django.core.mail import send_mail
import datetime
from django.contrib.auth.models import User 
from django.utils.timesince import timesince
from django.contrib           import messages
# Register your models here.

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class BaseSetting(object):
    enable_themes  = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "首页信息", "content": "<h1> 欢迎登陆同济大学教务管理系统! </h1><p><h2>陈良波开发维护中 </h2><br/>电话 : 18817870013</p>"},
            # {"type": "chart", "model": "app.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2013-01-08', 'p': 1, '_p_date__lt': '2013-01-29'}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start", "btns": [{"model":Student}, {"model":Lesson},{'title': "本研一体化系统", 'url': "http://4m3.tongji.edu.cn"}]},
        ],
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)

class GlobalSetting(object):
    site_title = "教务系统0.0"
    site_footer  = "Tongji University"
    global_search_models = [Student, Teacher, ]
    global_models_icon = {
              Student : 'fa fa-laptop',
              Teacher : 'fa fa-cloud',
    }

    menu_style = 'default'  # 'accordion'
 
    def get_site_menu(self):
        return (
            {"title": "选课管理", "icon": "fa fa-cloud","Lesson": self.get_model_perm(Lesson, "change"), "menus":(
                {"title": "学生信息", "url": self.get_model_url(Student, "changelist")},
                {"title": "教师信息", "url": self.get_model_url(Teacher, "changelist")},
                {"title": "课程信息", "url": self.get_model_url(Lesson, "changelist")},      
                {"title": "我的选课", "url": self.get_model_url(MyLessonTable, "changelist")},

            )},
            {"title":"基础信息","icon":"fa fa-cloud","Academy": self.get_model_perm(Academy, "change"), "menus":(
              {"title": "学院信息", "url": self.get_model_url(Academy, "changelist")},
              {"title": "专业信息", "url": self.get_model_url(Prefession, "changelist")},
              {"title": "用户类别", "url": self.get_model_url(UserProfile, "changelist")},
            )},
            {"title": "课程时间配置", "icon": "fa fa-cloud","Lesson": self.get_model_perm(LessonTime, "change"), "menus":(
              {"title": "上课日", "url": self.get_model_url(Weekday, "changelist")},
              {"title": "课程序号", "url": self.get_model_url(LessonNumber, "changelist")},
              {"title": "上课时间", "url": self.get_model_url(LessonTime, "changelist")},
            )},            
        )
   
xadmin.site.register(views.CommAdminView, GlobalSetting)


style = {"list_display" :'tuple' ,"fields": 'tuple',"readonly_fields":'list',
        "list_filter":'list',"search_fields":'list'}

class UserProfileAdmin(object):
    list_display  = ('id','user','userType')
    fields        = ('id','user','userType')
    list_filter   = ['id','user','userType']


class AcademyAdmin(object):
    list_display = ('id','name')

class PrefessionAdmin(object):
    list_display = ('id','academy','name')
    search_fields = ['academy',]
    list_filter   = ['academy',]

class WeekdayAdmin(object):
    list_display = ('id','wweek')


class LessonNumberAdmin(object):
    list_display = ('id','number1','number2','number3','number4')

class TeacherAdmin(object):
    list_display = ('id','username','name','userID','position','academy')

class StudentAdmin(object):
    list_display  = ('id','username','name','userID','academy','prefession','enterTime','year','state','tutor')

class LessonTimeAdmin(object):
    list_display = ('id','tweek','number1','number2','number3','number4')
    # style_fields  = {'tnumber':'m2m_transfer'}


class LessonAdmin(object):
    list_display = ('id','name','lessonID','teacher','listener','place','season','ltime','note')  #'ltime1','ltime2','ltime3',
    style_fields  = {"ltime":"m2m_transfer"}


class MyLessonTableAdmin(object):
    list_display = ('id','mylesson')


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Academy,AcademyAdmin)
xadmin.site.register(Prefession,PrefessionAdmin)
xadmin.site.register(Weekday,WeekdayAdmin)
xadmin.site.register(LessonNumber,LessonNumberAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(Student,StudentAdmin)
xadmin.site.register(LessonTime,LessonTimeAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(MyLessonTable,MyLessonTableAdmin)