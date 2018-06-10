#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:53:40 2018

@author: vagnercazarotto
"""

#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','green']
pHit = 0.6
pMiss = 0.2



def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        print(hit)
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(p)):
        q[i]=q[i]/s 
    return q

for k in range(len(measurements)):
    p = sense(p,measurements[k])

print(p)