#!/usr/bin/python

import sys,os
from time import sleep


os.system('.//src')
o=open('fin.txt','r')
oo=o.readlines()
#print oo
ww=[]
for i in oo:
    ww.append(i[:-1])

print 'Current Module nust be Behinded: ' , ww

for i in ww:
    print i

try:
    ww.remove('pcnet32')
    print 'Networking is Activated'
except:
    print 'Not Found'

for i in ww:
    print 'Deatach module %s\n' % i
    os.system('modprobe -r %s' % i)
    sleep(0.5)
