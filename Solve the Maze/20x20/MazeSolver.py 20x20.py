import cv2
import numpy as np

filename = '20x20'
img = cv2.imread(filename+'.png')
cv2.imshow('Maze', img)

# Binary conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Inverting tholdolding will give us a binary image with a white wall and a black background.
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV) 
cv2.imwrite(filename+'/1. Threshold1.jpg', thresh)
cv2.imshow('Threshold 1', thresh)

# Contours
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
dc = cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)
cv2.imwrite(filename+'/2. Contours1.jpg', dc)
cv2.imshow('Contours 1', dc)

dc = cv2.drawContours(dc, contours, 1, (0,0,0) , 5)
cv2.imwrite(filename+'/3. Contours2.jpg', dc)
cv2.imshow('Contours 2', dc)

ret, thresh = cv2.threshold(dc, 240, 255, cv2.THRESH_BINARY)
cv2.imwrite(filename+'/4. Threshold2.jpg', thresh)
cv2.imshow('Threshold 2', thresh)

ke = 19
kernel = np.ones((ke, ke), np.uint8)

# Dilate


dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imwrite(filename+'/5. Dilation.jpg', dilation)
cv2.imshow('Dilation', dilation)

# Erosion


erosion = cv2.erode(dilation, kernel, iterations=1)
cv2.imwrite(filename+'/6. Erosion.jpg', erosion)
cv2.imshow('Erosion', erosion)

# Find differences between two images
diff = cv2.absdiff(dilation, erosion)
cv2.imwrite(filename+'/7. Difference.jpg', diff)
cv2.imshow('Difference', diff)

# splitting the channels of maze


# Write code for splitting channels of Maze



# In order to display the solution on the original maze image, first divide the original maze into r, g, b components.
# Now create a mask by inverting the diff image.
# The bitwise and r and g components of the original maze using the mask created in the last step.
# This step will remove the red and green components from the image portion of the maze solution.
# The last one is to merge all the components and we will use the blue marked solution.

# masking out the green and red colour from the solved path
r = cv2.bitwise_and(r, r, mask=mask_inv)
b = cv2.bitwise_and(b, b, mask=mask_inv)

res = cv2.merge((b, g, r))
cv2.imwrite(filename+'/9. SolvedMaze.jpg', res)
cv2.imshow('Solved Maze', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
