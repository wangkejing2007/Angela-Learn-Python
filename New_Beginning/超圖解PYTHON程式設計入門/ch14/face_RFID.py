import serial
from webcam import Face

dataset_file = 'dataset\\staff.dat'  # 請自行修改路徑
user_id = 0

COM_PORT = 'COM9'  # 請自行修改序列埠名稱
BAUD_RATES = 230400
ser = serial.Serial(COM_PORT, BAUD_RATES)

def get_RFID(id):
    global user_id
    user_id = id
    print('使用者的RFID:', id)

    # 點亮控制板的綠燈
    ser.write(b'PASS\n')

    if ser.in_waiting:
        RFID_str = ser.readline().decode()
        tag_id = int(RFID_str, base=16)
        print('掃描到的RFID：', tag_id)

        if tag_id == user_id:
            ser.write(b'OPEN\n')
            print('門打開了！')
        else:
            print('卡片比對錯誤！')

        ser.flushInput()

face = Face(dataset_file, get_RFID)
face.start()