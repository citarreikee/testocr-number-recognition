import cv2 

img = cv2.imread('001.jpg')
cv2.imshow("box",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
