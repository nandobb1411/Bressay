import cv2 as cv

# Read image
img = cv.imread(r'bressay\data\lines\0013\0013_01_01.png')

# Display image
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow('Image', img)