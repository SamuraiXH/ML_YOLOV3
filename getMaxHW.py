import os
import cv2
#dir1 ,dir2 分别存储不同的数据集合,根据自己的需要修改
dir1='.\Image\\'
dir2 = '\Image\\'
height=0
width=0
for filename in os.listdir(dir1):
    img=cv2.imread(dir1+filename)
    sp = img.shape
    if(sp[0]>height):
        height=sp[0]
        print(filename)
    if(sp[1]>width):
        width=sp[1]
        print(filename)
print("h"+str(height)+"w"+str(width))
for filename in os.listdir(dir2):
    img=cv2.imread(dir2+filename)
    sp=img.shape
    if(sp[0]>height):
        height=sp[0]
    if(sp[1]>width):
        width=sp[1]
print("h"+str(height)+"w"+str(width))