# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:16:11 2017

@author: XMKZ

"""

import pylab as pl
import math

x=[0]
y=[0]
pi=math.pi
F=0.99
theta=0.2
q=0.5
omega=0.
l=9.8
g=9.8
od=2.0/3.0
t=0.
dt=0.01
while t<80:
    omega=omega-(math.sin(theta)+q*omega-F*math.sin(od*t))*dt
    theta=theta+omega*dt
    t=t+dt
    if theta>=pi:
        theta=theta-2*pi
    if theta<=-pi:
        theta=theta+2*pi
    x.append(t)
    y.append(theta)
    plot=pl.plot(x,y,'-',label='aaa')
pl.title('hahaha')
pl.xlabel('Time')
pl.ylabel('theta')
pl.xlim(0,80)
pl.ylim(-3,3)
pl.show()
        