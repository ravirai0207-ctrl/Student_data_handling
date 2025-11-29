#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 21:31:55 2025

@author: raviprakashrai
"""

import addnew
import find
with open("stu.txt", "r") as file:
    p = file.read()
    
    
""""
    Hi, im ravi making my second project. In this project i have made an interface 
    where school authorities can add, find and display student roll no, name, course
    & marks.
"""


print("Welcome to School's Portal\nWhat do You Want?\n1.Add student's marks\n2. display it?")
a=int(input("Answer in 1 or 2: "))
if(a==1):
    addnew.add(addnew.inp())
    print("Student's data sucessfully stored")
elif(a==2):
    print("1.Want all students data for cource\n2.A student data in all cources")
    print("3.A student data in specific cource")
    b=int(input(": "))
    if(b==1):
        r=input("Enter cource name for  which you want data of: ")
        find.pnt(find.findsub(p,r))
    elif(b==2):
        r=int(input("Enter Student roll no for  which you want data of: "))
        find.pnt(find.findall(p,str(r)))
    elif(b==3):
        q=int(input("Enter Student roll no for  which you want data of: "))
        r=input("Enter cource name for  which you want data of: ")
        find.pnt(find.findsp(p,str(q), r))
    else:
        print("Wrong Input")
else:
    print("Wrong Input")