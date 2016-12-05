# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser
from django.db import models
import datetime
import myChoise
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# user information
class UserProfile(models.Model):
    id       =  models.AutoField('id', primary_key=True)
    user     =  models.ForeignKey(User,verbose_name = "用户")
    userType =  models.IntegerField('用户类别', choices = myChoise.myUserType ,null = False,blank = False )

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户类别'
        verbose_name_plural = verbose_name

class Academy(models.Model):
    id       = models.AutoField('id', primary_key=True)
    name     = models.CharField('学院名称', blank=False,null = False, max_length = 100)

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'academy'
        verbose_name = '学院'
        verbose_name_plural = verbose_name

class Prefession(models.Model):
    id       = models.AutoField('id', primary_key=True)
    academy  = models.ForeignKey(Academy,verbose_name = "学院")
    name     = models.CharField('专业名称', blank=False,null = False, max_length = 100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'prefssion'
        verbose_name = '专业'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    id        = models.AutoField('id', primary_key=True)
    username  = models.ForeignKey(User,verbose_name = "用户名")
    name      = models.CharField('姓名',blank=False,null = False, max_length = 30)
    userID    = models.CharField('工号',blank=False,null=False,max_length=20)
    position  = models.CharField('职称',max_length = 20,blank=True,null=True)
    academy   = models.ForeignKey(Academy,verbose_name = "学院")
    def __unicode__(self):
        return u'教师-' + self.name

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name


class Student(models.Model):
    id        = models.AutoField('id', primary_key=True)
    username  = models.ForeignKey(User,verbose_name = "用户名")
    name      = models.CharField('姓名', blank=False,null = False, max_length = 30)
    userID    = models.CharField('学号',blank=False,null=False,max_length=20)
    academy   = models.ForeignKey(Academy,verbose_name = "学院")
    prefession = models.ForeignKey(Prefession,verbose_name = "专业")
    enterTime = models.DateField('入学时间', null=False, blank=False)
    year      = models.FloatField('学制',choices = myChoise.myState,max_length = 10,default = 2.5)
    state     = models.IntegerField('年级',null = False,blank = False )
    tutor     = models.ForeignKey(Teacher,verbose_name = "导师")

    def __unicode__(self):
        return u'学生-' + self.name

    class Meta:
        db_table = 'student'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


class Weekday(models.Model):
    id    = models.AutoField('id', primary_key=True)
    wweek = models.CharField('上课日',unique=True,max_length=40,null = False,blank = False )

    def __unicode__(self):
        return self.wweek

    class Meta:
        db_table = 'weekday'
        verbose_name = '上课日'
        verbose_name_plural = verbose_name

class LessonNumber(models.Model):
    id       = models.AutoField('id', primary_key=True)
    number1  = models.CharField('序号1',max_length =20,null = False,blank = False,default = '第1节')
    number2  = models.CharField('序号2',max_length =20,null = True,blank = True )
    number3  = models.CharField('序号3',max_length =20,null = True,blank = True )
    number4  = models.CharField('序号4',max_length =20,null = True,blank = True )
    
    def __unicode__(self):
        return self.number1 + self.number2 + self.number3 + self.number4

    class Meta:
        db_table = 'lesson_number'
        verbose_name = '课程序号'
        verbose_name_plural = verbose_name


class LessonTime(models.Model):
    id       = models.AutoField('id', primary_key=True)
    tweek    = models.ForeignKey(Weekday,db_column='tweek',related_name='tweek',null=False,blank=False,verbose_name = '上课日')
    number1  = models.CharField('序号1',max_length =20,null = False,blank = False,default = '第1节')
    number2  = models.CharField('序号2',max_length =20,null = True,blank = True )
    number3  = models.CharField('序号3',max_length =20,null = True,blank = True )
    number4  = models.CharField('序号4',max_length =20,null = True,blank = True )

    def __unicode__(self):
        return self.tweek.wweek + '-' + self.number1 + self.number2 + self.number3 + self.number4

    class Meta:
        db_table = 'lesson_time'
        verbose_name = '上课时间'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    id       = models.AutoField('id', primary_key=True)
    name     = models.CharField(u'课程名称', blank=False,null = False, max_length = 30)
    lessonID = models.CharField(u'课程编号',blank=False,null=False,max_length=20)
    teacher  = models.ForeignKey(Teacher,verbose_name = u"上课教师",blank=True,null=True)
    listener = models.IntegerField(u'开课年级',null = True,blank = True)
    place    = models.CharField(u'上课教室',blank=True,null=True,max_length=20)
    season   = models.IntegerField(u'开课季节',choices =myChoise.mySeason,blank=True)
    ltime    = models.ManyToManyField(LessonTime,db_column='ltime',related_name='ltime',blank=True,null=True,verbose_name=u'上课时间')
    # ltime    = models.ForeignKey(LessonTime,db_column='ltime',related_name='ltime',blank=True,null=True,verbose_name=u'上课时间')
    note     = models.CharField(u'备注',max_length=100,blank=True,null=True)

    def __unicode__(self):
        return self.name +'-'+ self.lessonID

    class Meta:
        db_table = 'lesson'
        verbose_name = u'课程信息'
        verbose_name_plural = verbose_name


class MyLessonTable(models.Model):
    id        = models.AutoField('id', primary_key=True)
    mylesson  = models.ForeignKey(Lesson,db_column='mylesson',related_name='mylesson',null=True,verbose_name=u'选择课程')
    
    def __unicode__(self):
        return str(self.mylesson)

    class Meta:
        db_table = 'mylesson_table'
        verbose_name = u'我的已选课程'
        verbose_name_plural = verbose_name


