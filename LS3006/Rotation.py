#!/usr/bin/env python

# Servo Control
import time
import RPi.GPIO as GPIO
import sys

#Setting global (Oh noz! Not globalz!) vars:
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(0)


#This class controls a robotic claw (Gripper Kit #637094) in various manners in order to interact with real-world objects. 
#It uses standard servo motor Duty Cycle calculations:
#
#http://www.toptechboy.com/raspberry-pi/raspberry-pi-lesson-28-controlling-a-servo-on-raspberry-pi-with-python/
#
#The above URL explains the calculations behind a 180 degree servo. The difference between that and the LS-3006 continious rotation
#servo is the closer you are to the nuetral duty (near 90 on a scale of 0-180), the slower the servo rotates.

class Grip:

	#Rotate clockwise in a relatively gentle manner
	def open(self):
		open_duration = 2.5
		duty = 82
		grip_cycle = (duty / 18.0) + 2.0
		print("Current Duty Cycle: {0}".format(grip_cycle))
		p.ChangeDutyCycle(grip_cycle)
		time.sleep(open_duration)

	#Rotate counter-clockwise in a relatively gentle manner
	def close(self):
		close_duration = 2.0
		duty = 100
		grip_cycle = (duty / 18.0) + 2.0
		print("Current Duty Cycle: {0}".format(grip_cycle))
		p.ChangeDutyCycle(grip_cycle)
		time.sleep(close_duration)

	#Allow parameters to provise intimate control over the servo speed and timing to allow any range of various
	#operations within the claws 4 inch grip. This is to mainly allow super precise operational parameters to
	#be provided in case this setup is ever used to defuse a dirty bomb, handle bio-agents, etc. Ultimate flexibility!
	def precise_move(self, duration, duty):
		grip_cycle = (duty / 18.0) + 2.0
		print("Current Duty Cycle: {0}".format(grip_cycle))
		p.ChangeDutyCycle(grip_cycle)
		time.sleep(duration)

	#We initiate a hold here. The higher the duty, the more pressure the "grip" of the servo exhibits against the object it holds.
	#Duration is self explanatory. 
	def hold(self, duration, duty):
		grip_cycle = (duty / 18.0) + 2.0
		print("Current Duty Cycle: {0}".format(grip_cycle))
		p.ChangeDutyCycle(grip_cycle)
		time.sleep(duration)
		
	#Pretty much the "main" method...
	def start(self, type, duration=None, duty=None):
		if type == "open":
			Grip().open()
		elif type == "close":
			Grip().close()
		elif type == "precise":
			try:
				grip_cycle = (duty / 18.0) + 2.0
				print("Current Duty Cycle: {0}".format(grip_cycle))
				p.ChangeDutyCycle(grip_cycle)
				time.sleep(duration)
			except Exception as e:
				print(e)
		else:
			print("You fucking suck. Use proper parameters")
			sys.exit(1)


g = Grip()
g.start("close")
g.hold(5, 130)
g.start("precise", .3, 75)
