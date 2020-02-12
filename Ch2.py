import numpy
import cv2

panda_image = cv2.imread("./images/panda.jpg")
panda_gray_image = cv2.cvtColor(panda_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray panda", panda_gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
