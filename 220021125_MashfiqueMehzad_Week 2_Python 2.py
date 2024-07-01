import os
import cv2

img_name = input()
img = cv2.imread(img_name)

filters = {
    'grayscale': cv2.COLOR_BGR2GRAY,
    'hsv': cv2.COLOR_BGR2HSV,
    'ycrcb': cv2.COLOR_BGR2YCrCb,
    'hls': cv2.COLOR_BGR2HLS,
    'luv': cv2.COLOR_BGR2LUV,
}

filename, ext = os.path.splitext(img_name)
for filter in filters:
    cv2.imwrite(f"{filename}-{filter}{ext}", cv2.cvtColor(img, filters[filter]))

cv2.imwrite(f"{filename}-guassian_blur{ext}", cv2.GaussianBlur(img, (9, 9), 10))