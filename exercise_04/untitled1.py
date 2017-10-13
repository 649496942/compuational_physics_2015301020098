# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 00:14:10 2017

@author: XMKZ
"""

v=4
t=0
delta=0.0001
a=4
c=0.0001
while t<=200:
    t=t+delta
    v=v+400*0.7*delta/(70*v)-0.5*0.7*1.225*0.33*v*v*delta/140
    a=a+400*c/(70*a)-0.5*1.225*0.33*a*a*c/140
    if t>=20 and a-v<=0.1:
        break
print(t)