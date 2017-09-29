# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:03:22 2017

@author: XMKZ
"""

import numpy
import pylab as py
N=1000
delta=0.01
Time=0
a=15
b=0.015
x=[0]
y=[0]
while Time<=0.999:
    Time=Time+delta
    N=N+(a*N-b*N**2)*delta
    x.append(Time)
    y.append(N)
else:
    plot=py.plot(x,y,'.',label='N')
    py.title('model')
    py.xlabel('Time')
    py.ylabel('N')
    py.xlim(0,1)
    py.ylim(0,2000)
    py.legend(loc='best')
    py.show()
