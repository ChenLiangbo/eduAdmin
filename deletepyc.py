# -*- coding: utf-8 -*-

import os

try:
    filedir = os.sys.argv[1]
    filedir = os.getcwd() +'/'+ filedir
except:
    print ("input a correct file directory!")

def removeOnedir(onedir):
    filelist = os.listdir(onedir)
    for f in filelist:
        filename = onedir + '/' + f
        if os.path.isfile(filename) and '.pyc' in f:
            os.remove(filename)
    for f in os.listdir(onedir):
        filename = os.path.basename(onedir) +'/' + f
        if os.path.isdir(filename):
            removePycfile(filename)

def removePycfile(filedir):
    filedir = os.path.basename(filedir)
    filelist = os.listdir(filedir)
    for f in filelist:
        filename = filedir + '/' + f
        if os.path.isdir(filename):
            removeOnedir(filename)
    return None

if __name__ == '__main__':
    removePycfile(filedir)