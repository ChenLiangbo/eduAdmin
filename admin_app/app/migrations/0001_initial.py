# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-29 11:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='\u5b66\u9662\u540d\u79f0')),
            ],
            options={
                'db_table': 'academy',
                'verbose_name': '\u5b66\u9662',
                'verbose_name_plural': '\u5b66\u9662',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('lessonID', models.CharField(max_length=20, verbose_name='\u8bfe\u7a0b\u7f16\u53f7')),
                ('listener', models.IntegerField(blank=True, null=True, verbose_name='\u5f00\u8bfe\u5e74\u7ea7')),
                ('place', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u4e0a\u8bfe\u6559\u5ba4')),
                ('season', models.IntegerField(blank=True, choices=[(0, '\u6625\u5b63'), (1, '\u79cb\u5b63')], verbose_name='\u5f00\u8bfe\u5b63\u8282')),
                ('note', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'lesson',
                'verbose_name': '\u8bfe\u7a0b\u4fe1\u606f',
                'verbose_name_plural': '\u8bfe\u7a0b\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='LessonNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('number1', models.CharField(default='\u7b2c1\u8282', max_length=20, verbose_name='\u5e8f\u53f71')),
                ('number2', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u53f72')),
                ('number3', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u53f73')),
                ('number4', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u53f74')),
            ],
            options={
                'db_table': 'lesson_number',
                'verbose_name': '\u8bfe\u7a0b\u5e8f\u53f7',
                'verbose_name_plural': '\u8bfe\u7a0b\u5e8f\u53f7',
            },
        ),
        migrations.CreateModel(
            name='LessonTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('number1', models.CharField(default='\u7b2c1\u8282', max_length=20, verbose_name='\u5e8f\u53f71')),
                ('number2', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u53f72')),
                ('number3', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u53f73')),
                ('number4', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5e8f\u53f74')),
            ],
            options={
                'db_table': 'lesson_time',
                'verbose_name': '\u4e0a\u8bfe\u65f6\u95f4',
                'verbose_name_plural': '\u4e0a\u8bfe\u65f6\u95f4',
            },
        ),
        migrations.CreateModel(
            name='MyLessonTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('mylesson', models.ForeignKey(db_column='mylesson', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mylesson', to='app.Lesson', verbose_name='\u9009\u62e9\u8bfe\u7a0b')),
            ],
            options={
                'db_table': 'mylesson_table',
                'verbose_name': '\u6211\u7684\u5df2\u9009\u8bfe\u7a0b',
                'verbose_name_plural': '\u6211\u7684\u5df2\u9009\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Prefession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='\u4e13\u4e1a\u540d\u79f0')),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Academy', verbose_name='\u5b66\u9662')),
            ],
            options={
                'db_table': 'prefssion',
                'verbose_name': '\u4e13\u4e1a',
                'verbose_name_plural': '\u4e13\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('userID', models.CharField(max_length=20, verbose_name='\u5b66\u53f7')),
                ('enterTime', models.DateField(verbose_name='\u5165\u5b66\u65f6\u95f4')),
                ('year', models.FloatField(choices=[(2.5, 2.5), (4, 4), (5, 5), (7, 7)], default=2.5, max_length=10, verbose_name='\u5b66\u5236')),
                ('state', models.IntegerField(verbose_name='\u5e74\u7ea7')),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Academy', verbose_name='\u5b66\u9662')),
                ('prefession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Prefession', verbose_name='\u4e13\u4e1a')),
            ],
            options={
                'db_table': 'student',
                'verbose_name': '\u5b66\u751f\u4fe1\u606f',
                'verbose_name_plural': '\u5b66\u751f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('userID', models.CharField(max_length=20, verbose_name='\u5de5\u53f7')),
                ('position', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u804c\u79f0')),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Academy', verbose_name='\u5b66\u9662')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d')),
            ],
            options={
                'db_table': 'teacher',
                'verbose_name': '\u6559\u5e08\u4fe1\u606f',
                'verbose_name_plural': '\u6559\u5e08\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('userType', models.IntegerField(choices=[(0, '\u7cfb\u7edf\u7ba1\u7406\u5458'), (1, '\u5b66\u751f'), (2, '\u6559\u5e08')], verbose_name='\u7528\u6237\u7c7b\u522b')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'db_table': 'user_profile',
                'verbose_name': '\u7528\u6237\u7c7b\u522b',
                'verbose_name_plural': '\u7528\u6237\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('wweek', models.CharField(max_length=40, unique=True, verbose_name='\u4e0a\u8bfe\u65e5')),
            ],
            options={
                'db_table': 'weekday',
                'verbose_name': '\u4e0a\u8bfe\u65e5',
                'verbose_name_plural': '\u4e0a\u8bfe\u65e5',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='\u5bfc\u5e08'),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AddField(
            model_name='lessontime',
            name='tweek',
            field=models.ForeignKey(db_column='tweek', on_delete=django.db.models.deletion.CASCADE, related_name='tweek', to='app.Weekday', verbose_name='\u4e0a\u8bfe\u65e5'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='ltime',
            field=models.ForeignKey(blank=True, db_column='ltime', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ltime', to='app.LessonTime', verbose_name='\u4e0a\u8bfe\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='\u4e0a\u8bfe\u6559\u5e08'),
        ),
    ]
