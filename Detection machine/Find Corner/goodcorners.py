import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image then grayscale
image = cv2.imread('../../images/chess.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


temp_output = image.copy()

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(10, 5))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Input')
cv2.imwrite('input.jpg', image)

# specifying the top 50 corners
# Write its code here

axs[1].imshow(cv2.cvtColor(temp_output, cv2.COLOR_BGR2RGB))
axs[1].set_title('Good Corners Found')
cv2.imwrite('good_corners_found.jpg', temp_output)

plt.show()