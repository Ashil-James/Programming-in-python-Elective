import cv2

img = cv2.imread('cyber_logopng.png')
# Add border to the image

border = cv2.copyMakeBorder(
    img,
    top = 50,
    bottom = 50,
    left = 50,
    right = 50,
    borderType = cv2.BORDER_REFLECT,
    value = [0, 0, 255]
)

cv2.imshow('Bordered Image', border)
cv2.waitKey(0)
cv2.destroyAllWindows()