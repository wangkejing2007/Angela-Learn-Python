import time
from machine import Pin
import urequests as req

led = Pin(2, Pin.OUT, value=1)
sw = Pin(0, Pin.IN)

apiURL = '{url}?key={key}&id={id}'.format(
    url='https://你的伺服器網址/btn',
    key='zzzzz',
    id='wash_dish'
)

while True:
    if sw.value() == 0:
        time.sleep_ms(20)
        led.value(0)
        req.get(apiURL)  # 連結到LINE伺服器網址
        while sw.value() == 0:
            pass
