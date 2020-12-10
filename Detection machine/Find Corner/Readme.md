## 💥Detection of Corners

This can be done using two methods:
#### ▶Harris Corner Detection
Harris Corner Detection is an algorithm developed in 1998 for corner detection (http://www.bmva.org/bmvc/1988/avc-88-023.pdf) and works fairly well.
cv2.cornerHarris(input image, block size, ksize, k)

1.Input image - should be grayscale and float32 type.

2.blockSize - the size of neighborhood considered for corner detection

3.ksize - aperture parameter of Sobel derivative used.

4.k - harris detector free parameter in the equation

5.Output – array of corner locations (x,y)

The output of the detection of Harris Corner is below:

<img src="https://github.com/supu2701/Open-CV-Projects/blob/main/Images/img9.png">

#### ▶Good Corner feature
This is an improved corner detection feature
cv2.goodFeaturesToTrack(input image, maxCorners, qualityLevel, minDistance)

1.Input Image - 8-bit or floating-point 32-bit, single-channel image.

2.maxCorners – Maximum number of corners to return. If there are more corners than are found, the strongest of them is returned.

3.qualityLevel – Parameter characterizing the minimal accepted quality of image corners. The parameter value is multiplied by the best corner quality measure (smallest eigenvalue).
The corners with the quality measure less than the product are rejected. For example, if the best corner has the quality measure = 1500, and the qualityLevel=0.01 , then all the corners with the quality - - measure less than 15 are rejected.

4.minDistance – Minimum possible Euclidean distance between the returned corners.

The output of the detection of Good corner feature is shown below:

<img src="https://github.com/supu2701/Open-CV-Projects/blob/main/Images/img10.png">

#### Corners as features:
There are certain problems with corners as features:

✔Corner matching in images is tolerant of:
1. Rotations

2. Translations(i.e shifts in image)

3. Slight photometric changes e.g brightness or affine intensity

✔Corner matching is intolerant of
1. Large chances in intensity or photometric chnages.
2. Scaling( enlarging or shrinking)
