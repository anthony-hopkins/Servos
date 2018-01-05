#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

class Kill:
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	def kill(self):
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, False)
		GPIO.cleanup()

Kill().kill()
