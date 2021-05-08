#Minimum Cost Spanning Tree
"""
Created on Sun May 17 06:03:34 2020

@author: shyam
"""
#weighted graph:4x4
wtgraph=[[0,20,0,90],[2,0,100,10],[0,100,0,40],[90,10,40,0]]

#Display wtgraph
for row in range(4):
    for col in range(4):
        print(wtgraph[row][col],end=" ")
    print(" ")
#start=input("Enter the starting vertex:")
#vxt=[start]
vx=[1,2,3,4]
vxt=[1,2]
ed=[None]
edt=[None]
v=len(vx)
#list of all possible edges
for i in range(4):
    for j in range(4):
        ed=[vx[i],vx[j]]
        print(ed,end=" ")
               
#original vx set, tree vertex set
def remainvx(vx,vxt):
    for i in range(len(vxt)):
        for j in range(len(vx)):
            if vxt[i]==vx[j]:
                vx.remove(vx[j])
                return vx
#pass search_element, array_list_to_be_searched           
def ifpresent(n,list):
    for item in list:
        if n==item:
            return True
        else:
            return False
#pass an edge        
def edwt(ed):
    row=ed[0][0]
    col=ed[0][1]
    return wtgraph[row][col]

#pass edge set        
def minwtedge(ed,vx,vxt):
    minedge=[None]
    minedge=ed[0]   
    for i in range(len(vxt)):
        for j in range(len(vx)):
            currentedge=ed[i]  #change later
            if ifpresent(i,vxt) and ifpresent(j,vx):#if vx present in tree_vx and orig_vx
                if(edwt(minedge)>edwt(currentedge)):
                    minedge=currentedge   
            #vxt=vxt.append(minedge[0])
            vxt=vxt.append(vx[j])
            vx=remainvx(vx,vxt)
    return minedge 
            
#actual s*it starts here lmao
for i in range(v):
    minwted=minwtedge(ed,vx,vxt)
"""    vxt=vxt.append(minwted[0][1])
    edt=edt.append(minwted)
"""    
                

  
"""for i in range(v):
    minwt(vxt,vxo)"""
    
"""
#to find minimum edge
def minwtedge(ed):
    minedge=ed[0]
    for i in range(len(ed)):
    
        if(minedge>ed[i]):
            minedge=ed[i]
            return minedge    
 """     
        
            

    
    
 

    
         