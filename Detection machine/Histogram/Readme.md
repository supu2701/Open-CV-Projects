## 🛑Histogram Detection🛑
This feature is called Histogram of Oriented Gradients(HOG)

1. HOG are a feature descriptor that has been widely and successfully used for object detection.

2. It represents object as a single vector feature as opposed to a set of feature vectors where each represents a segment iof the image.

3. It is computed by sliding window detector over an image, where a HOG Descriptor is computed for ech position. Like SIFT, the scale of the image is adjusted.

4. HOG are often used with SVM(support vector machine) classifiers. Each HOG Descriptor that is computed is fed to a SVM Classifier to determine if the object was found or not.

### ⭕Tech Guide
http://stackoverflow.com/questions/6090399/get-hog-image-features-from-opencv-python
http://www.juergenwiki.de/work/wiki/doku.php?id=public:hog_descriptor_computation_and_visualization

## ⭕Original input and its Gradient Output

<img src="https://github.com/supu2701/Open-CV-Projects/blob/main/Images/img7.png">

<img src="https://github.com/supu2701/Open-CV-Projects/blob/main/Images/img8.png">
