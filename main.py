import cv2
import numpy as np

image = cv2.imread("D:\dog2.jpg")

cv2.imshow("oriinal", image)

grey_dog = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GREY", grey_dog)
print(grey_dog.shape)

B, G, R = cv2.split(image)
print(B.shape)

cv2.imshow("red image", R)
cv2.imshow("blue image", B)
cv2.imshow("green image", G)

merge = cv2.merge([R, G, B])

blur = cv2.blur(image, (5, 5))
Gaussianblur = cv2.GaussianBlur(image, (5, 5), 0)

image4 = cv2.Canny(image, 40, 100)
kernal = np.ones((5, 5), np.uint8)
image5 = cv2.erode(image, kernal, iterations=1)
image6 = cv2.dilate(image, kernal, iterations=1)

image7 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernal)
image8 = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernal)

kernal1 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])

image9 = cv2.filter2D(image, -1, kernal1)

cv2.imshow("blur", blur)
cv2.imshow("GBLUR", Gaussianblur)
cv2.imshow("sketch", image4)
cv2.imshow("Erosion", image5)
cv2.imshow("Dilation", image6)
cv2.imshow("Morph close", image7)
cv2.imshow("Morph open", image8)
cv2.imshow("sharpen", image9)
cv2.imshow("merged", merge)
cv2.waitKey()
cv2.destroyAllWindows()



