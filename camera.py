import cv2

cam = cv2.VideoCapture(3)

while True:
    ret, image = cam.read()
    cv2.imshow('Imagetest',image)
    cv2.imwrite('/home/pi/tflite1/test1.jpg', image)
    k = cv2.waitKey(1)
    if k != -1:
        break
cam.release()
cv2.destroyAllWindows()