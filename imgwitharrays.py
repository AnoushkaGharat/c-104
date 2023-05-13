import cv2
import numpy as np
black= np.zeros([600,600])

frow = black[1:2]
print(frow)

fcolumn=black[:,1:2]
print(fcolumn)

black[200:400,200:400] = 255
print(black)

cv2.imshow("Black Image",black)
print(black)
cv2.waitKey(0)