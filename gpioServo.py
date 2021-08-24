import readchar
from gpiozero import Servo
from time import sleep

servo = Servo(20)

while 1:
    key = readchar.readkey()
    print(key)
    if key == 'q':
        break
    if key == 'd':
        servo.max()
    if key == 'a':
        servo.min()
    if key == '':
        servo.max()
    if key == 's':
        servo.min()

