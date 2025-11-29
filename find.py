#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 16:48:30 2025

@author: raviprakashrai
"""

#a student data in all cources
def findall(p,q):
    a=p.split("  ")
    c=[]
    for i in range(0,len(a)-1):
        j=a[i].split()
        if(j[0]==q):
            c.append(j)
    return c
#A student data in specific cource
def findsp(p,q,r):
    a=p.split("  ")
    c=[]
    for i in range(0,len(a)-1):
        j=a[i].split()
        if(j[0]==q):
            c.append(j)
    for i in range(0,len(c)):
        if(c[i][2]==r):
            return [c[i]]
#All student data in specific cources
def findsub(p,r):
    a=p.split("  ")
    b=[]
    for i in range(0,len(a)-1):
        c=a[i].split()
        if(c[2]==r):
                b.append(c)
    return b
def pnt(a):
    c=["Roll No=> ","Name=> ","Cource=> ","Marks=> "]
    for i in range(0,len(a)):
        print("===============================================")
        b=a[i]
        for j in range(0,len(b)):
            print(c[j],b[j])
