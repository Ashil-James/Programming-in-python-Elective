import cv2

img = cv2.imread('cyber_logopng.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#bw using normal thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Otsu's method — automatically finds the best threshold value
_, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive threshold — uses local neighborhood (handles uneven lighting)
adaptive = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize = 11,
    C = 2
)

cv2.imshow('Original', img)
cv2.imshow('Binary Threshold', thresh)
cv2.imshow('Otsu Threshold', otsu_thresh)
cv2.imshow('Adaptive Threshold', adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()