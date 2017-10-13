# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:01:26 2017

@author: XMKZ
"""

import pylab as pl
v=4
t=0
delta=0.01
x=[0]
y=[0]
while t<=200:
    t=t+delta
    v=v+400*0.7*delta/(70*v)-0.5*0.7*1.225*0.33*v*v*delta/140
    x.append(t)
    y.append(v)
else:
    pl.plot(x,y,'r-',label='middle')

a=4
b=0
c=0.0001
x=[0]
y=[0]
while b<=200:
    b=b+c
    a=a+400*c/(70*a)-0.5*1.225*0.33*a*a*c/140
    x.append(b)
    y.append(a)
else:
    pl.plot(x,y,'b--',label='front')
pl.title('velocity/time')
pl.xlabel('T/s')
pl.ylabel('V m/s')
pl.xlim(0,200)
pl.ylim(0,20)
pl.show()
