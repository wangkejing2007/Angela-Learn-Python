import cv2
import face_recognition as fr
import numpy as np
from PIL import ImageDraw, Image

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    img_arr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_PIL = Image.fromarray(img_arr)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    face_loc = fr.face_locations(small_frame)
    draw = ImageDraw.Draw(img_PIL)

    for loc in face_loc:
        top, right, bottom, left = loc
        top    *= 4
        right  *= 4
        bottom *= 4
        left   *= 4
        draw.rectangle(((left,top),(right,bottom)), outline='blue')

    img_CV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    cv2.imshow('Webcam', img_CV)

    if cv2.waitKey(1) & 0xFF == 27: # 按ESC鍵退出
        break

cam.release()
cv2.destroyAllWindows()