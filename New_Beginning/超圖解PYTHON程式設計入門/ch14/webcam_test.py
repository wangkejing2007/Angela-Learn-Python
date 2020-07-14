from webcam import Face

dataset_file = 'dataset\\staff.dat'

def get_RFID(id):
    print('使用者的RFID:', id)

face = Face(dataset_file, get_RFID)
face.start()