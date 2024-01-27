# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:26:50 2024

@author: GEMMA
"""
import random
TOTAL_POINTS=100000000000
xs=[]
ys=[]
pt=0
for i in range(TOTAL_POINTS):
		xs.append(random.randint(0,1000))
		ys.append(random.randint(0,1000))
for i in range(TOTAL_POINTS):
    if(xs[i]*xs[i]+ ys[i]*ys[i])<10000000:
        pt=pt+1

MonteCarlopi=pt/TOTAL_POINTS*4.0

print('pi:'+ str(MonteCarlopi))

