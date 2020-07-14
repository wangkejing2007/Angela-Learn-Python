from machine import Pin
import time

state = False

LED = Pin(2, Pin.OUT)
PIR = Pin(5, Pin.IN)

try:
    while True:
        if PIR.value() == 1:
            LED.value(0)

            if state == False:
                print('Motion detected')
                state = True  
        else:
            LED.value(1)

            if state == True:
                print('Motion stopped!')
                state = False

except KeyboardInterrupt:
    print('bye!')