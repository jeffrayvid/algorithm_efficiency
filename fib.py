# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 13:54:16 2018

@author: Yofftop
"""

import time

#exponential running time
def fib1(n):
	if n==0:
		return 0
	if n==1 or n==2:
		return 1
	else:
		return (fib1(n-1)+fib1(n-2))

#linear running time
def fib2(n):
	f = [0]*(n+1)
	f[0]=0
	f[1]=1
	for i in range (2,n):
		f[i] = f[i-1]+f[i-2]
	return f[n-1]

#Revise the fib.py to add a third function that calculate Fn 
#in linear time and constant space(memory)
def fib3(n):
    first=0
    second=1
    if n==1:
        return first
    if n==2:
        return second
    else:
        for i in range(2,n):
            Nth=first+second
            first=second
            second=Nth
        return second

for i in range(1,50):
	start_time = time.time();
	res = fib3(i)
	end_time = time.time();
	elapsed_time = end_time - start_time;
	print(i,':',elapsed_time, ':', res)
