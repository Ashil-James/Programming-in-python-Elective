import cv2


img = cv2.imread('cyber_logopng.png')

blur = cv2.blur(img, (5, 5))

# Gaussian blur — center pixels get more weight, natural-looking
gauss = cv2.GaussianBlur(img, (5, 5), sigmaX=0)

# Median blur — replaces pixel with MEDIAN of neighbors (best for salt & pepper noise)
median = cv2.medianBlur(img, 5)

# Bilateral filter — blurs BUT preserves edges (slow but beautiful)
bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow('Original', img)
cv2.imshow('Blur', blur)
cv2.imshow('Gaussian Blur', gauss)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()