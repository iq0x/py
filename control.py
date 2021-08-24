import readchar
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(7.5)

i = 1

while 1:
    i += 1
    key = readchar.readkey()
    print(key)
    if key == 'q':
        break
    if key == 'd':
        try:
            while True:
                p.ChangeDutyCycle(7.5) #90
                time.sleep(1)
                p.ChangeDutyCycle(12.5) #180
                time.sleep(1)

        except KeyboardInterrupt:
            p.stop()


GPIO.cleanup()
