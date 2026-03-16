import cv2

img = cv2.imread('cyber_logopng.png')

h, w = img.shape[:2]

# FLIP
flip_h = cv2.flip(img, 1)   #  1 = horizontal (left-right mirror)
flip_v = cv2.flip(img, 0)   #  0 = vertical   (upside down)
flip_b = cv2.flip(img, -1)  # -1 = both axes

# ─── ROTATE ─────────────────────────────────────────
center = (w // 2, h // 2)

M_90  = cv2.getRotationMatrix2D(center, angle=90,  scale=1.0)
M_180 = cv2.getRotationMatrix2D(center, angle=180, scale=1.0)
M_45  = cv2.getRotationMatrix2D(center, angle=45,  scale=1.0)

rot_90  = cv2.warpAffine(img, M_90,  (w, h))
rot_180 = cv2.warpAffine(img, M_180, (w, h))
rot_45  = cv2.warpAffine(img, M_45,  (w, h))

# ─── CROP ────────────────────────────────────────────
# img[y1:y2, x1:x2]  — rows first, then columns
cropped = img[50:300, 100:400]   # rows 50–300, cols 100–400

# Crop center of the image
cx, cy = w // 2, h // 2
size   = 100  # half-size of crop box
crop_center = img[cy - size : cy + size, cx - size : cx + size]

# ─── RESIZE ──────────────────────────────────────────
# Fixed size
resized_fixed = cv2.resize(img, (640, 480))

# Scale by percentage
resized_half   = cv2.resize(img, None, fx=0.5, fy=0.5)   # 50%
resized_double = cv2.resize(img, None, fx=2.0, fy=2.0)   # 200%

# Resize keeping aspect ratio
target_w = 300
ratio     = target_w / w
resized_ar = cv2.resize(img, (target_w, int(h * ratio)))

# ─── DISPLAY ALL ─────────────────────────────────────
cv2.imshow('Original',       img)
cv2.imshow('Flip Horizontal',flip_h)
cv2.imshow('Flip Vertical',  flip_v)
cv2.imshow('Flip Both',      flip_b)
cv2.imshow('Rotate 90',      rot_90)
cv2.imshow('Rotate 180',     rot_180)
cv2.imshow('Rotate 45',      rot_45)
cv2.imshow('Cropped',        cropped)
cv2.imshow('Crop Center',    crop_center)
cv2.imshow('Resize Fixed',   resized_fixed)
cv2.imshow('Resize Half',    resized_half)
cv2.imshow('Resize AR',      resized_ar)

cv2.waitKey(0)
cv2.destroyAllWindows()

