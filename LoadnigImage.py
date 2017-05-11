import numpy as np
import cv2

#Loading an image from file

img = cv2.imread("svindal.jpg", cv2.IMREAD_GRAYSCALE)

#showing the image in a window

cv2.imshow("Axel lund Svindal", img)
cv2.waitKey(0)
cv2.destroyAllWindows()