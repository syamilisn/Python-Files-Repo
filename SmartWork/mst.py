# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:26:29 2020

@author: shyam
"""
vx=[1,2,3,4]
vxt=[1,2]
ed=[[0,0]]
ed.remove([0,0])
edt=[None]
v=len(vx)
vt=len(vxt)
wtgraph=[[0,20,0,90],[2,0,100,10],[0,100,0,40],[90,10,40,0]]
for i in range(4):
    for j in range(4):
        if ed.count([vx[i],vx[j]]) <1:
            ed.append([vx[i],vx[j]])
            print(ed)
        #print(ed,end=" ")
        
        
print(ed[0][1])       
def edwt(ed):
    row=ed[0][0]
    col=ed[0][1]
    return wtgraph[row][col]
        
def ifpresent(n,list):
    for item in list:
        if n==item:
            return True
        else:
            return False
        
def remainvx(vx,vxt):
    for i in range(len(vxt)):
        for j in range(len(vx)):
            if vxt[i]==vx[j]:
                vx.remove(vx[j])
                return vx      
            
def minwtedge(ed,vx,vxt):
    minedge=[None]
    minedge=ed[0]  
    k=0
    for i in range(v):  #4
        for j in range(v): #4
            currentedge=ed[k]  #change later      k=0
            if ifpresent(i+1,vxt) and ifpresent(j+1,vx):#if vx present in tree_vx and orig_vx
                if(edwt(minedge)>edwt(currentedge)):
                    minedge=currentedge 
            if k<=len(ed):
                k=k+1
            #vxt=vxt.append(minedge[0])
            vxt=vxt.append(vx[j])
            print("Tree vx:",len(vxt))
            vx=remainvx(vx,vxt)
            print("Orig vx:",len(vx))
    return minedge 
       
for i in range(v):
    minwted=minwtedge(ed,vx,vxt)