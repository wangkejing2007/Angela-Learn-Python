import mfrc522
from machine import Pin
from machine import UART
import time

BAUD_RATES = 230400
mode = Pin(4, Pin.IN)  # 第4腳預設是高電位
DOOR_PIN = Pin(2, Pin.OUT, value=1)
GREEN_LED = Pin(5, Pin.OUT)
RFID_code = b''

# sck, mosi, miso, rst, cs
rdr = mfrc522.MFRC522(14, 13, 12, 16, 15)

def open_door():
	DOOR_PIN.value(0)      # 開門（點亮內建的LED）
	time.sleep(0.5)
	DOOR_PIN.value(1)

def serial_com():
	com = UART(0, BAUD_RATES)
	com.init(BAUD_RATES)

	while True:
		choice = com.readline()
		stat, _ = rdr.request(rdr.REQIDL)
		
		if choice == b'PASS\n':
			GREEN_LED.value(1)    # 代表人臉辨識過關
		elif choice == b'OPEN\n':
			open_door()      	  # 開門
		else:
			GREEN_LED.value(0)
		
		if stat == rdr.OK:
			stat, raw_uid = rdr.anticoll()

			if stat == rdr.OK:
				RFID_code = b'0x{0:02x}{1:02x}{2:02x}{3:02x}\n'.format(
							  raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]
							)
				com.write(RFID_code)


def read_tag():
	print("\nRFID reader running...\n")
	
	try:
		while True:
			stat, tag_type = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:
				stat, raw_uid = rdr.anticoll()

				if stat == rdr.OK:
					print("RFID detected")
					print("  - tag type: 0x{:02x}".format(tag_type))
					print("  - uid	 : 0x{0:02x}{1:02x}{2:02x}{3:02x}".format(
							raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
						 )
					print("")

	except KeyboardInterrupt:
		print("Bye")

def main():
    if mode.value():
        serial_com()
    else:
        read_tag()

if __name__ == '__main__':
    main()