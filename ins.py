#Read an image with opencv2

import sys
import cv2
print("OpenCV version :",cv2.__version__)

image1 = cv2.imread(sys.argv[0])
cv2.imshow('BidIdea Image', image1)
cv2.waitKey(0) 

print(image1)
print('Type:', type(image1))
print('Dimensions:', image1.shape)
print('Top-left pixel RGB :', image1[0,0])

print('Complete')

