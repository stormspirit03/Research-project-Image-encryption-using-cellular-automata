#!/usr/bin/env python
# coding: utf-8

# In[2]:

from PIL import Image
import numpy as np 
import cv2 
import matplotlib.pyplot as plt


# In[3]:


img=cv2.imread('Lenna.png')


# In[4]:


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[5]:


plt.imshow(img)


# In[6]:


iar=np.asarray(img)
#print(iar)


# In[7]:


#print(iar)


# In[8]:


len(iar)


# In[9]:


plt.imshow(img)


# In[10]:


#taking average value and subtracting sum from 255
row, col = iar.shape[0], iar.shape[1]
newiar=np.zeros((row, col,3),dtype='uint8')

for j in range(0,col):
    newiar[0,j,0]=iar[0,j,0]
    newiar[0,j,1]=iar[0,j,1]
    newiar[0,j,2]=iar[0,j,2]

for j in range(0,col):
    newiar[row-1,j,0]=iar[row-1,j,0]
    newiar[row-1,j,1]=iar[row-1,j,1]
    newiar[row-1,j,2]=iar[row-1,j,2]
    
for i in range(1,row-1):
    newiar[i,0,0]=iar[i,0,0]
    newiar[i,0,1]=iar[i,0,1]
    newiar[i,0,2]=iar[i,0,2]
    newiar[i,col-1,0]=iar[i,col-1,0]
    newiar[i,col-1,1]=iar[i,col-1,1]
    newiar[i,col-1,2]=iar[i,col-1,2]
	
sum_red=0
sum_green=0
sum_blue=0
for i in range(1,row-1):
    for j in range(1,col-1):
        sum_red=0
        sum_green=0
        sum_blue=0
        for k in range(i-1,i+2):
            sum_red=sum_red+iar[k,j-1,0]+iar[k,j,0]+iar[k,j+1,0]
            sum_green=sum_green+iar[k,j-1,1]+iar[k,j,1]+iar[k,j+1,1]
            sum_blue=sum_blue+iar[k,j-1,2]+iar[k,j,2]+iar[k,j+1,2]
        newiar[i,j,0]=255-sum_red/9
        newiar[i,j,1]=255-sum_green/9
        newiar[i,j,2]=255-sum_blue/9

#print(newiar)


# In[11]:


len(newiar)


# In[12]:




# In[13]:


plt.imshow(img)


# In[14]:


iar[0][0][0]


# In[15]:


iar[0][0][0]


# In[16]:


"""li2=[]
for i in range(256):
    li1=[]
    for j in range(256):
        li=[]
        for k in range(3):
            #abc=bin(iar[i][j][k]).replace("08","")
            #li.append(bin(iar[i][j][k]).replace("08b",""))
            #li.append("{0:8b}".format(iar[i][j][k]))
            
            li.append(format(iar[i][j][k],'b').zfill(8))
         
             
            
        li1.append(li)
    li2.append(li1)
#print(li2)
#list(li2)"""
    
    


# In[253]:



#a=list(li2[0][0][0])
#print(a)
#n = [int(i) for i in a]
#print(n)



# In[17]:


li5=[]
for i in range(512):
    li4=[]
    for j in range(512):
        li3=[]
        for k in range(3):
            #abc=bin(iar[i][j][k]).replace("08","")
            #li.append(bin(iar[i][j][k]).replace("08b",""))
            #li.append("{0:8b}".format(iar[i][j][k]))
            b=list(format(iar[i][j][k],'b').zfill(8))
            
            li3.append([int(q) for q in b] )
         
             
            
        li4.append(li3)
    li5.append(li4)
#print(li5)


#list(li2)


# In[ ]:





# In[391]:


"""li5=[]
for i in range(101,256):
    li4=[]
    for j in range(101,256):
        li3=[]
        for k in range(3):
            #abc=bin(iar[i][j][k]).replace("08","")
            #li.append(bin(iar[i][j][k]).replace("08b",""))
            #li.append("{0:8b}".format(iar[i][j][k]))
            c=list(format(iar[i][j][k],'b').zfill(8))
            
            li3.append([int(d) for d in c] )
         
             
            
        li4.append(li3)
    li5.append(li4)
print(li5)
#list(li2)"""


# In[264]:


###li5[0][0][0]


# In[422]:


import itertools
def XOR(x,y,z):
    if x!=z:
        return 1
    else:
        return 0

def NOT(x):
    if x == 1:
        return 0
    else:
        return 1

def R90(p,q,r): #Working
    return XOR(p,q,r)

def R102(p,q,r): #Working
    return XOR(p,q,r)

def R153(p,q,r):
    return NOT(q)*NOT(r) + q*r

def R254(p,q,r):
    return 1 - (1 - p)*(1 - q)*(1 - r)

def R250(p,q,r):
    return p + r - p * r


def R30(p,q,r): #Working
    return (p + q + r + q * r)% 2

def R110(p,q,r):
    return ((1 + p) * q * r + q + r)

def R130(p,q,r):
    return NOT(p)*NOT(q)*r + p*q*r

def R156(p,q,r):
    return NOT(p)*q + p*q*r + p*NOT(q)*NOT(r)

def R51(p,q,r):
    a = NOT(q)
    return a

#{51,51,51,102,153,153,51,156}

#print(R156(0,1,1))

'''
a = 5
b =int(input("Enter"))
c = a+b
print(c)
d = c%2
print(d)
'''

'''
R90 = R90(1,0,1)
R30 = R30(1,0,1)
Fun_R = [R90,R30]
a = [1,2,3,4]
b = []
sum = 0
for i in range(1,len(a)+1):
   b.append(list(itertools.combinations(a,i)))
for i in b:
    for k in i:
        for j in k:
            sum = sum + j
            print(sum)
print(b)
'''

# In[437]:

from rules import *
import numba as nb
#Rec = False

#Input by user
'''for i in range(0,8):
    j = int(input(""))
    IV.append(j)
'''
#@nb.jit(nopython=True)
def HashFunC(L,time,RV):
    j = 0
    IV1 = L[:]
    IV2 = []
    x = 0
    RV = False
    Rec = False
    IV = L[:]
    #print(IV)
    #print(IV)
    #print("Generation 0")
    #print(IV)
    #Cycles should be a minimum of 8 else Error
    for j in range(1,time):
        if Rec == True:
            #print("End")
            return j-1,IV
            break
        x = 0
        IV2.clear()
        for i in IV:
            if x == 0:
                a = 0
                b = i
                c = IV[x+1]
                #print(a,b,c,"-->",R30(a,b,c))
                #print("R90")
                IV2.append(R90(a,b,c))
                x = x+1
            else:
                if x == 7:
                    a = IV[x-1]
                    b = i
                    c = 0
                    #print(a,b,c,"-->",R30(a,b,c))
                    if RV == False:
                        #print("R90")
                        IV2.append(R90(a,b,c))
                    else:
                        #print("R30")
                        IV2.append(R30(a,b,c))
                    #print("Generation",j)
                    #print(IV2)
                    if IV2 == IV1:
                        
                        #print(IV2)
                        Rec = True
                        IV = IV2[:]
                        break
                    IV = IV2[:]
                    break
                else:
                    a = IV[x-1]
                    b = i
                    c = IV[x+1]
                    #print(a,b,c,"-->",R30(a,b,c))
                    if RV == False:
                        #print("R90")
                        IV2.append(R90(a,b,c))
                    else:

                        if x == 1:
                            #print("R30")
                            IV2.append(R30(a,b,c))
                        elif x == 2:
                            #print("R90")
                            IV2.append(R90(a,b,c))
                        elif x == 3:
                            #print("R30")
                            IV2.append(R30(a,b,c))
                        elif x == 4:
                            #print("R90")
                            IV2.append(R90(a,b,c))
                        elif x == 5:
                            #print("R30")
                            IV2.append(R30(a,b,c))
                        elif x == 6:
                            #print("R90")
                            IV2.append(R90(a,b,c))

                    x = x+1
    return j,IV

list1=[]
for i in range(512):
    list2=[]
    for j in range(512):
        list3=[]
        for k in range(3):
            #list3.append((HashFunC(li5[i][j][k],2,False))[1])
            #print(HashFunC(li5[i][j][k],2,False))
            #abc=bin(iar[i][j][k]).replace("08","")
            #li.append(bin(iar[i][j][k]).replace("08b",""))
            #li.append("{0:8b}".format(iar[i][j][k]))
            
            #int("".join(str(x) for x in (HashFunC(li5[i][j][k],2,False))[1]), 2)
            list3.append(int("".join(str(x) for x in (HashFunC(li5[i][j][k],15,False))[1]), 2))
        list2.append(list3)
    list1.append(list2)
   # print(HashFunC(li5[i][j][k],10000,False))
print(list1)
#print(HashFunC([1,1,1,1,1,1,1,1],10000000,False))


# In[429]:


#plt.imshow(img)


# In[438]:


#print(len(li5))
#print(list1)
#print(len(list1))
#print(list1[511][511])
#print(list1)
#print(np.asarray(list1))
abc=np.asarray(list1)
#pqr=Image.fromarray(abc)
#pqr.save('newlenna.png')
#abc=cv2.cvtColor(abc,cv2.COLOR_RGB2BGR)

#img1=cv2.cvtColor(abc,cv2.COLOR_BGR2RGB)
cv2.imwrite('newagter8gjnwejn.jpg', img1)
