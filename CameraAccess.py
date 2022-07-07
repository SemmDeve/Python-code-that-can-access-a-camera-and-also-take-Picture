import cv2

cam = cv2.VideoCapture(0)

while (True):
    ret, frame = cam.read()

    cv2.imshow("frame", frame)

    image_take = "image_test/test.png"
    cv2.imwrite(image_take, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  


cam.release()

cam.destoryAllWindows()