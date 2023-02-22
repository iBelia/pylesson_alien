import cv2

img = cv2.imread('ship_new.bmp')
h, w, c = img.shape
new_size = (int(w*0.5), int(h*0.5))
img_resize = cv2.resize(img, new_size)
cv2.imwrite('new_ship_1.bmp', img_resize)


