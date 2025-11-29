#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 16:15:46 2025

@author: raviprakashrai
"""

def inp():
    r=int(input("Roll No."))
    n=input("Enter name")
    c=input("course Name: ")
    d=float(input("Marks ; "))
    return r,n,c,d

def add(r):
    p=""+str(r[0])+" "+r[1]+" "+r[2]+" "+str(r[3])+"  "
    with open("stu.txt", "a") as file:
        file.write(p)
