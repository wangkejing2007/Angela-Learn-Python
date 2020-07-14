import cv2
import face_recognition
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pickle

font_file = "font\\NotoSansCJKtc-Regular.otf"   # 請自行修改路徑

class Face:
    def __init__(self, dataset, callback=None, tolerance=0.6):
        self.callback = callback
        self.tolerance = tolerance
        with open(dataset, 'rb') as f:
            d = pickle.load(f)
            self.face_encodings = d['encode']
            self.face_names = d['name']
            self.face_ids = d['RFID']
    
    def start(self):
        _vid = cv2.VideoCapture(0)
        _font = ImageFont.truetype(font_file, 15)
        process_this_frame = True
        face_loc = None

        while True:
            _, frame = _vid.read() 
            img_PIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, 
                                                                 face_locations)

                for i, face_encoding in enumerate(face_encodings):
                    matches = face_recognition.compare_faces(
                              self.face_encodings, 
                              face_encoding, 
                              tolerance=self.tolerance)
                    name = "不明人士"
                    face_id = 0

                    if True in matches:
                        index = matches.index(True)
                        name = self.face_names[index]
                        face_id = self.face_ids[index]
                        face_loc = face_locations[i]

                        if self.callback:   # 傳回此使用者的RFID值
                            self.callback(face_id)

                        break

            process_this_frame = not process_this_frame

            draw = ImageDraw.Draw(img_PIL)

            if face_loc:
                top, right, bottom, left = face_loc
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
                _, text_height = draw.textsize(name, font=_font)
                draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
                draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255), font=_font)
                
            img_OpenCV = cv2.cvtColor(np.asarray(img_PIL),cv2.COLOR_RGB2BGR)
            cv2.imshow('Video', img_OpenCV)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        _vid.release()
        cv2.destroyAllWindows()