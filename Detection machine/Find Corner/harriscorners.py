# Library Imports 
import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Global Variables 
kernel_size=3

def harrisCornersDetection(imgPath,N=100,goodFeatures=False,flag=True,row=1,col=2,plot=False):
    image=cv2.imread(imgPath)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    temp_output=image.copy()
    
    if(goodFeatures):
        corners = cv2.goodFeaturesToTrack(gray,N,0.01,10)
        corners = np.int0(corners)
        for i in corners:
            x,y=i.ravel()
            cv2.circle(temp_output,(x,y),6,255,-1)
        cv2.imwrite('Good_Corners.jpg', temp_output)
    
    else: 
        hc=cv2.cornerHarris(gray,blockSize=2,ksize=3,k=0.04)
        dil=cv2.dilate(hc,kernel=np.ones((kernel_size,kernel_size)),iterations=1)
        ret,dst=cv2.threshold(dil,0.01*dil.max(),255,0)
        temp_output[dst>0.01*dst.max()]=[0,0,255]
        cv2.imwrite('Harris_Corners.jpg', temp_output)
    
    if(plot):
        row,col=row,col
        fig,axs=plt.subplots(row,col,figsize=(10,5))
        fig.tight_layout()
        axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        axs[0].set_title('Original Input')
        axs[1].imshow(cv2.cvtColor(temp_output, cv2.COLOR_BGR2RGB))
        axs[1].set_title('Corners')
        plt.show()
              
if __name__=='__main__':
    harrisCornersDetection('input.jpg',goodFeatures=False,plot=True,flag=True)


 

