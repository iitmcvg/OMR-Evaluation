# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 17:02:36 2017

@author: Vishwesh

Program reads a scanned sheet of OMR of particular institution and creates a text file of response with roll no:, set no: and answers

Completed on :4th April 2017 
"""

import cv2
import numpy as np


img_rgb = cv2.imread('14.jpg')


#for bringing down the size
ratio=1000.0/img_rgb.shape[0]
dimension=(540,int(ratio*img_rgb.shape[1]))

img_rgb=cv2.resize(img_rgb,dimension,interpolation=cv2.INTER_AREA)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template1.jpg',0)
w, h = template.shape[::-1]

#for mathing the squares
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
shapex=np.zeros((10),dtype=np.int32)
shapey=np.zeros((10),dtype=np.int32)
i=0

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    shapex[i]=pt[0] 
    shapey[i]=pt[1]
    i=i+1

z=0
l=0

#for removing repeated coordinates
for l in range (0,10): 
  
    for z in range (1,10-l):
        
        if abs(shapex[l]-shapex[l+z])<3 and abs(shapey[l]-shapey[l+z])<3 :
            shapex[l+z]=0  
            shapey[l+z]=0     
       


#for sorting wrt x coordinates
for i in range (0,10):
    for j in range (0,10-i-1):
        if shapex[j]>shapex[j+1]:
            temp=shapex[j]
            shapex[j]=shapex[j+1]
            shapex[j+1]=temp
            temp=shapey[j]
            shapey[j]=shapey[j+1]
            shapey[j+1]=temp
    
        if shapex[j]==shapex[j+1] and shapey[j]>shapey[j+1] :
            temp=shapex[j]
            shapex[j]=shapex[j+1]
            shapex[j+1]=temp
            temp=shapey[j]
            shapey[j]=shapey[j+1]
            shapey[j+1]=temp    



for pt in range (6,10):
    cv2.rectangle(img_rgb, (shapex[pt],shapey[pt]), (shapex[pt] + w, shapey[pt] + h), (255,255,0), 0)       



#perspective transformation
pts1 = np.float32([[shapex[6]+h,shapey[6]+w],[shapex[8]+h,shapey[8]+w],[shapex[7]+h,shapey[7]+w],[shapex[9]+h,shapey[9]+w]])           
pts2 = np.float32([[0,0],[700,0],[0,700],[700,700]])
M = cv2.getPerspectiveTransform(pts1,pts2)
img_rgb = cv2.warpPerspective(img_rgb,M,(700,700))







bubbletemplate=cv2.imread('bubbletemplate.png',0)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

w, h = bubbletemplate.shape[::-1]
res = cv2.matchTemplate(img_gray,bubbletemplate,cv2.TM_CCOEFF_NORMED)
threshold = 0.805 #to avoid faint marking put threshold=0.87 and half ellipse=0.80

bubx=np.zeros((1500),dtype=np.int32)# stores all bubble coordinates including repeated same coordinates
buby=np.zeros((1500),dtype=np.int32)
bub1x=np.zeros((1500),dtype=np.int32) #stores all unique bubble coordinates
bub1y=np.zeros((1500),dtype=np.int32)

#for dRAWING OUT LOCATIONS
loc = np.where( res >= threshold)



i=0

for pt in zip(*loc[::-1]):
    bubx[i]=pt[0]
    buby[i]=pt[1]
    i=i+1

i=0  
k=0  


for pt in zip(*loc[::-1]):   
    
    j=0
    flag=1
    for j in range(1,20):
             if abs(bubx[i]-bubx[i+j])<3 and abs(buby[i]-buby[i+j])<3:
                 flag=0
    j=0
    if flag!=0: 
        bub1x[k]=pt[0]
        bub1y[k]=pt[1]
        k=k+1        
    i=i+1

#to read omr result

   
sepx=np.zeros(k,dtype=np.int32) #To store value of seperation
sepy=np.zeros(k,dtype=np.int32)

for i in range(0,k-1): 
    sepy[i]=abs(bub1y[i]-bub1y[i+1])
    

#partions b/w roll no: section and answer response, finds that coordinate  
tempy=np.sort(sepy)
for z in range (0,k-1):
    if tempy[k-1]==sepy[z]:
            break
        
  
#for answer evaluation
omrsep=np.sort(sepy[z+1:k])  
quessep=omrsep[k-z-2]

F=open("Answer response.txt","w")


bub2x=np.zeros((30),dtype=np.int32) #stores coordinates of roll no:
bub2y=np.zeros((30),dtype=np.int32)
rollno=np.zeros((3),dtype=np.int32) 

i=0
k1=0




#to take out the example bubble filled out of the picture
for pt in bub1x[0:z+1]:
        if pt<350 and bub1y[k1]<=bub1y[z]:
              cv2.rectangle(img_rgb,(pt,bub1y[k1]),(pt+w,bub1y[k1]+h),(255,255,0),0)
              bub2x[i]=pt
              bub2y[i]=bub1y[k1]
              i=i+1
        k1=k1+1 



#bubble sort for x coordinates
for y in range (0,i):
    for m in range (0,i-y-1):
        if bub2x[m]>bub2x[m+1]:
            temp=bub2x[m]
            bub2x[m]=bub2x[m+1]
            bub2x[m+1]=temp
            temp=bub2y[m]
            bub2y[m]=bub2y[m+1]
            bub2y[m+1]=temp   
       
   

#roll no: detection
for y in range (0,i):
  mini=min(bub2y[0:i])
  if bub2x[y]<max(bub2x[0:i]):
    if bub2y[y]>=mini and bub2y[y]<(mini+0.8*h):
        rollno[y]=0
    if bub2y[y]>=mini+0.8*h and bub2y[y]<(mini+1.6*h):
        rollno[y]=1
    if bub2y[y]>=mini+1.6*h and bub2y[y]<(mini+2.4*h):
        rollno[y]=2
    if bub2y[y]>=mini+2.4*h and bub2y[y]<(mini+3.2*h):
        rollno[y]=3
    if bub2y[y]>=mini+3.2*h and bub2y[y]<(mini+4.0*h):
       rollno[y]=4
    if bub2y[y]>=mini+4.0*h and bub2y[y]<(mini+4.8*h):
       rollno[y]=5
    if bub2y[y]>=mini+4.8*h and bub2y[y]<(mini+5.6*h):
        rollno[y]=6
    if bub2y[y]>=mini+5.6*h and bub2y[y]<(mini+6.4*h):
        rollno[y]=7
    if bub2y[y]>=mini+6.4*h and bub2y[y]<(mini+7.2*h):
       rollno[y]=8
    if bub2y[y]>=mini+7.2*h and bub2y[y]<(mini+8.0*h):
       rollno[y]=9    
        
F.write ("ROLL NO: "+str(rollno[0])+str(rollno[1])+str(rollno[2])) 

#for finding set number
F.write("\n")
 
  
if bub2y[i-1]>=mini and bub2y[i-1]<(mini+0.8*h):
        F.write( "set 1")
if bub2y[i-1]>=mini+0.8*h and bub2y[i-1]<(mini+1.6*h):
         F.write( "set 2")
if bub2y[i-1]>=mini+1.6*h and bub2y[i-1]<(mini+2.4*h):
         F.write( "set 3")
if bub2y[i-1]>=mini+2.4*h and bub2y[i-1]<(mini+3.2*h):
         F.write( "set 4")


F.write("\n")
F.write("\n")
F.write("\n")



F.write("RESPONSE: \n")

def ansdetector(z,k,bub1x,w,h,x1,y1,quesno):
    for y in range (z+1,k):
    
        if bub1x[y]>=min(bub1x[z+1:])+x1*w and bub1x[y]<min(bub1x[z+1:])+y1*w:
           for n in range (1,21):   
               if bub1y[y]+h/2> bub1y[z+1]+(n-1)*h and bub1y[y]+h/2< bub1y[z+1]+(n)*h:
                   F.write("q" + str(n+quesno) + " ")
           
           cv2.rectangle(img_rgb, (bub1x[y],bub1y[y]), (bub1x[y]+ w,bub1y[y] + h), (255,255,0), 0)
           if bub1x[y]>=min(bub1x[z+1:])+x1*w and bub1x[y]<min(bub1x[z+1:])+(x1+1)*w:        
              F.write("A \n")
           if bub1x[y]>=min(bub1x[z+1:])+(x1+1)*w and bub1x[y]<min(bub1x[z+1:])+(x1+2)*w:    
              F.write("B \n") 
           if bub1x[y]>=min(bub1x[z+1:])+(x1+2)*w and bub1x[y]<min(bub1x[z+1:])+(x1+3)*w:    
              F.write("C \n")     
           if bub1x[y]>=min(bub1x[z+1:])+(x1+3)*w and bub1x[y]<min(bub1x[z+1:])+(x1+4)*w:    
              F.write("D \n")        
    return;







ansdetector(z,k,bub1x,w,h,1,5,0)
ansdetector(z,k,bub1x,w,h,7,11,20)
ansdetector(z,k,bub1x,w,h,14,18,40)
ansdetector(z,k,bub1x,w,h,20,24,60)
ansdetector(z,k,bub1x,w,h,27,31,80)
 

    



cv2.imshow('bubbledetected',img_rgb)
F.close()
cv2.waitKey(0)