#!/usr/bin/python

import RPi.GPIO as GPIO

print "start....."

GPIO.setmode(GPIO.BOARD);

GPIO.setup(18, GPIO.IN)

while True:
    input_value = GPIO.input(18)
    print "X: " + str(input_value)
