import serial
from time import sleep
import sys

COM_PORT = 'COM9'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)

try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        choice = input('按1人臉辨識過關、按2開門、按3回一般模式、按e關閉程式  ').lower()

        if choice == '1':
            print('傳送人臉辨識過關')
            ser.write(b'PASS\n')  # 訊息必須是位元組類型
            sleep(0.5)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        elif choice == '2':
            print('傳送開門指令')
            ser.write(b'OPEN\n')
            sleep(0.5)
        elif choice == '3':
            print('回一般模式')
            ser.write(b'NORMAL\n')
            sleep(0.5)
        elif choice == 'e':
            ser.close()
            print('再見！')
            sys.exit()
        else:
            print('指令錯誤…')

        while ser.in_waiting:
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            print('控制板回應：', mcu_feedback)
            
except KeyboardInterrupt:
    ser.close()
    print('再見！')