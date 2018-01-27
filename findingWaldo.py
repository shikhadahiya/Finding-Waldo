import cv2 as cv
import numpy as np

#load input image and convert to grayscale
image = cv.imread('/Users/shikhadahiya/Desktop/WaldoBeach.jpeg')
cv.imshow('Where is Waldo?', image)
cv.waitKey(0)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#load template image
template = cv.imread('/Users/shikhadahiya/Desktop/waldo.jpeg', 0)

result = cv.matchTemplate(gray, template, cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

#creating boudning rectangle
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv.rectangle(image, top_left, bottom_right, (0, 0, 255), 5)

cv.imshow('Where is Waldo?', image)
cv.waitKey(0)
cv.destroyAllWindows()