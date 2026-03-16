import cv2

# Load the image
image = cv2.imread('cyber_logopng.png')

# color to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg', gray)

# grayscale to color
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imwrite('gray_to_color.jpg', gray_bgr)

# With false color (heatmap style)
heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
cv2.imwrite('FalseColor.jpg', heatmap)




