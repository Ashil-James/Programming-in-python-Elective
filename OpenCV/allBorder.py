import cv2

img = cv2.imread("photo.jpg")

replicate = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REFLECT)
constant = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=[0,255,0])

cv2.imshow("Original", img)
cv2.imshow("Replicate", replicate)
cv2.imshow("Reflect", reflect)
cv2.imshow("Constant", constant)

cv2.waitKey(0)
cv2.destroyAllWindows()