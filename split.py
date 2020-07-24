# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:16:25 2019

@author: SELVAKUMAR
"""
a=[]
s=[]
domain=[]
id=[]
n=int(input("enter the no of mails:"))
for i in range(0,n):
    a=str(input("enter the string:"))
    s=a.split("@")
    domain.append(s[1])
    id.append(s[0])
for i in range(0,len(domain)):
    print("mails domain",domain[i])
    print("mails ID",id[i])
print("finish")