# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:10:48 2018

@author: Caden
"""

#设定要求最小硬币数的总钱数
S=121
#手中钱面值的种类
coin=[1,3,5]
#初始化所有值为S/(最小coin)
Min={}
for t in range(S+1)[1:]:
    Min[t]=round(S/min(coin))
Min[0]=0

for i in range(S+1)[1:]:
    for V_j in coin:
        if V_j<=i and Min[i-V_j]+1<Min[i]:
            Min[i]=Min[i-V_j]+1
   
print(Min[S])
