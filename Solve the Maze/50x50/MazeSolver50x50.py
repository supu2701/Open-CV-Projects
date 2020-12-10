'''
Requirements:
    Python3 Version
    OpenCV Version >=3
'''
#Library Imports 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Directory 
filename='50x50.png'

def MazeFunction(filename,kernel_size=19,show=False):
    
    #Read the img 
    img=cv2.imread(filename)

    if(show):
        cv2.imshow('Image',thresh)
        cv2.waitKey(0)

    #Convert to Grayscale & Thresholding
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite('Threshold1.jpg',thresh)
    if(show):
        cv2.imshow('Thresholding',thresh)
        cv2.waitKey(0)


    #Extract Contours
    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    dc=cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)
    cv2.imwrite('Contours1.jpg',dc)
    dc=cv2.drawContours(dc,contours,1,(0,0,0),5)
    cv2.imwrite('Contours2.jpg',dc)

    if(show):
        cv2.imshow('Final Contour',dc)
        cv2.waitKey(0)


    #Thresholding on the contour img
    ret, thresh = cv2.threshold(dc, 245, 255, cv2.THRESH_BINARY)
    cv2.imwrite('Threshold2.jpg', thresh)

    if(show):
        cv2.imshow('Thresholding on Contour', thresh)
        cv2.waitKey(0)

    #Kernel Settings
    kernel=np.ones((kernel_size,kernel_size),np.uint8)

    # Dilation
    dilation=cv2.dilate(dc,kernel,iterations=1)
    cv2.imwrite('Dilation.jpg',dilation)

    if(show):
        cv2.imshow('Dilation Operation',dilation)
        cv2.waitKey(0)

    #Erosion
    erosion=cv2.erode(dilation,kernel,iterations=1)
    cv2.imwrite('Erosion.jpg', erosion)

    if(show):
        cv2.imshow('Erosion Operation', erosion)
        cv2.waitKey(0)

    #Find differences between 2 images 
    diff = cv2.absdiff(dilation, erosion)
    cv2.imwrite('Difference.jpg',diff)

    if(show):
        cv2.imshow('Difference',diff)
        cv2.waitKey(0)

    #Statement Missing to show the difference 


    #Splitting the channels of Maze
    b, g, r = cv2.split(img)
    mask_inv = cv2.bitwise_not(diff)
    cv2.imwrite('Mask.jpg', mask_inv)

    if(show):
        cv2.imshow('Mask Inverse', mask_inv)
        cv2.waitKey(0)

    #Masking out the Green and Red colour from the solved path
    r = cv2.bitwise_and(r, r, mask=mask_inv)
    b = cv2.bitwise_and(b, b, mask=mask_inv)

    res = cv2.merge((b, g, r))
    cv2.imwrite('SolvedMaze.jpg', res)

    if(show):
        cv2.imshow('Solved Maze', res)
        cv2.waitKey(0)
    
    cv2.destroyAllWindows()

if __name__=='__main__':
    MazeFunction(filename)
