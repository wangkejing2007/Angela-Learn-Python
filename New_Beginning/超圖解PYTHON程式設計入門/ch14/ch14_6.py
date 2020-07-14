import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    # cv2.imshow('Webcam', frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 1)
    cv2.imshow('Webcam', gray)
    
    # if cv2.waitKey(1) == 27:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()