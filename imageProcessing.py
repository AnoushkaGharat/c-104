import cv2
img = cv2.imread("PRO-104-OpenCV-Image-Assets-main/butterfly.jpg")
cv2.imshow("Display Butterfly Image", img)
print(img)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Display Gray Butterfly Image",gray_img)
print(gray_img)
cv2.waitKey(0)