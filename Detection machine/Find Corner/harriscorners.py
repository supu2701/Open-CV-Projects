import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load image then grayscale
image = cv2.imread('../../images/chess.jpg')
#gray scale the image

temp_output = image.copy()

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(10, 5))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Input')
cv2.imwrite('input.jpg', image)

harris_corners = cv2.cornerHarris(gray, 3, 3, 0.05)

#We use dilation of the corner points to enlarge them\
# write code here

# Threshold for an optimal value, it may vary depending on the image.
#write code of temp_output

axs[1].imshow(cv2.cvtColor(temp_output, cv2.COLOR_BGR2RGB))
axs[1].set_title('Harris Corners')
cv2.imwrite('harris_corners.jpg', temp_output)

plt.show()