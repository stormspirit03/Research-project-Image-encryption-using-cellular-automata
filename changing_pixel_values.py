import numpy as np
import cv2
import matplotlib.pyplot as plt
# In[189]:
img=cv2.imread('lenna.png')#ADD YOUR IMAGE
# In[190]: img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # In[191]:
plt.imshow(img)
# In[192]:
iar=np.asarray(img) print(iar)
# In[193]:
iar[0][0][0]=0
# In[194]:
 print(iar)
# In[195]:
plt.imshow(img)
# In[209]:
#taking average value and subtracting sum from 255
row, col = iar.shape[0], iar.shape[1] newiar=np.zeros((row, col,3),dtype='uint8')
for j in range(0,col): newiar[0,j,0]=iar[0,j,0] newiar[0,j,1]=iar[0,j,1] newiar[0,j,2]=iar[0,j,2]
for j in range(0,col): newiar[row-1,j,0]=iar[row-1,j,0] newiar[row-1,j,1]=iar[row-1,j,1] newiar[row-1,j,2]=iar[row-1,j,2]
for i in range(1,row-1): newiar[i,0,0]=iar[i,0,0] newiar[i,0,1]=iar[i,0,1] newiar[i,0,2]=iar[i,0,2] newiar[i,col-1,0]=iar[i,col-1,0] newiar[i,col-1,1]=iar[i,col-1,1] newiar[i,col-1,2]=iar[i,col-1,2]
sum_red=0
sum_green=0
sum_blue=0
for i in range(1,row-1):
for j in range(1,col-1): sum_red=0
sum_green=0
sum_blue=0
for k in range(i-1,i+2):
sum_red=sum_red+iar[k,j-1,0]+iar[k,j,0]+iar[k,j+1,0] sum_green=sum_green+iar[k,j-1,1]+iar[k,j,1]+iar[k,j+1,1]
 
sum_blue=sum_blue+iar[k,j-1,2]+iar[k,j,2]+iar[k,j+1,2] newiar[i,j,0]=255-sum_red/9
newiar[i,j,1]=255-sum_green/9 newiar[i,j,2]=255-sum_blue/9
print(newiar)
imm = Image.fromarray(newiar) imm.save('my_pic.jpeg')
# In[210]:
plt.imshow(imm)