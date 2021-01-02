# ⭐💥 Image Processing Projects 💥⭐

## 🛑Project 1: Obstacle detection and shortest Route Planning🛑
Identifies the shortest path from the starting to end point using Image processing techniques using Open CV. This project aims at developing a mechanism to identify the shortest path leading to the destination and avoiding any kind of obstacle during robot’s traversal route. The file shortest_path_code using OpenCV and Shortest-Route(Detailed) contains python code consisting of required functions to detect the shortest route between the origin and the destination(denoted by blue box) as well as detect presence of obstacles if any(denoted by black boxes), on the path supposed to be traversed by any simulated bot.
The code checks for different sample cases uploaded in Test Images file. The file labelled delatiled shows the output in a detailed and self explinable manner consisting of the routes coordinates, obstacle coordinates, path lenght and the actual path taken.

### ⭕Given:

A set of test images, each containing

✔ 10x10 grid, making 100 squares
✔ Obstacles marked as black square
✔ Starting and ending point of route marked in blue boxes.



The squares are identified by the coordinate (x,y) where x is the column and y is the row to which the square belongs. Each square
can be empty or have an Obstacle or have an Object.

### ⭕The command window displays the following parameters: 
<img src="https://github.com/supu2701/Shortest-Route-using-Open-CV/blob/main/Path_3.PNG" />

1. Process points
2. Total Number of occupied grids
3. Coloured occupied grids
4. Total Number of coloured occupied grids
5. Dictionary keys of planned path
6. Coordinates of planned path

## 🛑Project 2: Solve the Maze🛑
This project aims at finding the solution of perfect mazes, which is defined as a maze that has only one path from any point in the maze to any other point. Also, maze has no in-accessible sections, no circular paths and no open areas. Maze images should have dark walls on light background.

### ⭕Algorithm to be used:⭕

✔ Loading and converting the source image to binary image
``` 
filename = '50x50'
img = cv2.imread(filename+'.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV) 
```
✔ Finding Contours
```
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
dc = cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)
dc = cv2.drawContours(dc, contours, 1, (0,0,0) , 5)
```
✔ Dilating Contours
``` 
kernel = np.ones((19, 19), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)
```
✔ Eroding the Dilated image by same amount
```
erosion = cv2.erode(dilation, kernel, iterations=1)
```
✔ Finding difference of two images
```
diff = cv2.absdiff(dilation, erosion)
```
✔ Drawing the obtained path on source images
```
b, g, r = cv2.split(img)
mask_inv = cv2.bitwise_not(diff)
r = cv2.bitwise_and(r, r, mask=mask_inv)
b = cv2.bitwise_and(b, b, mask=mask_inv)
res = cv2.merge((b, g, r))
```

### ⭕Files Present⭕

1. Test images file contains Mazes of different dimentions- 5*5, 20*20 and 50*50
2. Maze Solver.py conatains actual python code to solve the mazes
3. Different algorithm approaches to solve mazes of different dimentions.

## 🛑Project 3: Detection Machine🛑
This project aims to build the algorithm of a detector which can detect a face, people, car do tasks like finding corners, histogram of oriented gradients, identifying contours, car video detection and pedestrian video detection.

### ⭕Files Present:⭕
#### ✔Identify Contour-
This will detect contours contours are a useful tool for shape analysis and object detection and recognition.
#### ✔Find Corner-
To classify and or detect objects from an image, we need to find important features such as edges, corners (also known as interest points), or blobs (also known as regions of interest ). Corners are the intersection of two edges, it represents a point in which the directions of these two edges change. Hence, the gradient of the image (in both directions) have a high variation, which can be used to detect it.
#### ✔Histogram-
Detection of Histogram of oriented gradients.
The distribution ( histograms ) of directions of gradients ( oriented gradients ) are used as features. Gradients ( x and y derivatives ) of an image are useful because the magnitude of gradients is large around edges and corners ( regions of abrupt intensity changes ) and we know that edges and corners pack in a lot more information about object shape than flat regions.
#### ✔Face & Eye Detector-
 This detects Faces and Eyes in the images and from webcam. Use of Haar feature-based cascade classifiers which is one of the effective methods of object detection.
 This HAAR Cascade Classifiers is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

#### ✔Car video detector-
Car detection based on Haar-like classifiers, which is the most common technique in computer-vision for cars.
#### ✔Pedestrian Video Detection-
Pedestrian detection based on Haar-like classifiers, which is the most common technique in computer-vision for Pedestrian detection.

#### ✔Toonify Image-
A Python aplication which takes Image as input and toonify it i.e make a cartonist image of it.

## ⭕Tech stack guides⭕

- ✔ [Python 3 guide] (https://www.python.org/doc/):
- ✔ [Open CV] (https://docs.opencv.org/):
- ✔ [Git and Github] (https://guides.github.com/introduction/):

## ⭕How to Contribute?⭕
If you wish to help, you can learn more about how you can contribute to this project in the [contribution guide](CONTRIBUTING.md).


## Interesting? Star⭐ this Repo😊

# Happy Learning💯 Happy Developing👍

