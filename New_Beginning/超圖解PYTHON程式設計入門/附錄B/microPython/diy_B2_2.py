from machine import Pin
import time
import urequests as req

state = False
start_timer = True
delay_ms = 30 * 1000

LED = Pin(2, Pin.OUT)
PIR = Pin(5, Pin.IN)

LED.value(1)

apiURL = '{url}?key={key}&id={id}'.format(
    url='https://你的網址/btn',
    key='zzzzz',     # 請自行修改密碼
    id='front_door'  # 你可以自行修改「裝置代碼」
)

try:
    while True:
        if PIR.value() == 1:
            if state == False:
                LED.value(0)
                print('Motion detected')
                state = True
                req.get(apiURL)

        if state:
            if start_timer:
                print('start timer!')
                start = time.ticks_ms()
                start_timer = False

            delta = time.ticks_diff(time.ticks_ms(), start)

            if delta >= delay_ms:
                start_timer = True
                state = False
                LED.value(1)
                print('LED is OFF!')

except KeyboardInterrupt:
    LED.value(1)
    print('bye!')
