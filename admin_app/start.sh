#!/usr/bin/env bash

PROJDIR="`pwd`"
PIDFILE="`pwd`/adminapp.pid"

exec /usr/bin/env python manage.py runfcgi method=prefork host=127.0.0.1 port=7788 pidfile=$PIDFILE
