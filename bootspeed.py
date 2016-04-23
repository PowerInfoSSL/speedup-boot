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

print 'ww is: ' , ww

for i in ww:
    print i


for i in ww:
    print 'Deatach module %s\n' % i
    os.system('modprobe -r %s' % i)
    sleep(0.5)
