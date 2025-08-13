#!/usr/bin/env python

# Servo Control for LS-3006 Continuous Rotation Servo
import time
import RPi.GPIO as GPIO
import sys

# GPIO Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(0)

# LS-3006 Continuous Rotation Servo Control
# Uses standard servo duty cycle calculations with 180-degree scale
# Neutral position (90) = slowest rotation, extremes (0/180) = fastest rotation

class Grip:
    """Controls robotic claw (Gripper Kit #637094) for object interaction"""

    def open(self):
        """Rotate clockwise to open gripper"""
        open_duration = 2.5
        duty = 82
        grip_cycle = (duty / 18.0) + 2.0
        print(f"Current Duty Cycle: {grip_cycle}")
        p.ChangeDutyCycle(grip_cycle)
        time.sleep(open_duration)

    def close(self):
        """Rotate counter-clockwise to close gripper"""
        close_duration = 2.0
        duty = 100
        grip_cycle = (duty / 18.0) + 2.0
        print(f"Current Duty Cycle: {grip_cycle}")
        p.ChangeDutyCycle(grip_cycle)
        time.sleep(close_duration)

    def precise_move(self, duration, duty):
        """Execute precise movement with custom parameters"""
        grip_cycle = (duty / 18.0) + 2.0
        print(f"Current Duty Cycle: {grip_cycle}")
        p.ChangeDutyCycle(grip_cycle)
        time.sleep(duration)

    def hold(self, duration, duty):
        """Maintain grip pressure for specified duration"""
        grip_cycle = (duty / 18.0) + 2.0
        print(f"Current Duty Cycle: {grip_cycle}")
        p.ChangeDutyCycle(grip_cycle)
        time.sleep(duration)
        
    def start(self, type, duration=None, duty=None):
        """Main control method for servo operations"""
        if type == "open":
            Grip().open()
        elif type == "close":
            Grip().close()
        elif type == "precise":
            try:
                grip_cycle = (duty / 18.0) + 2.0
                print(f"Current Duty Cycle: {grip_cycle}")
                p.ChangeDutyCycle(grip_cycle)
                time.sleep(duration)
            except Exception as e:
                print(e)
        else:
            print("Use proper parameters...")
            sys.exit(1)

# Example usage
g = Grip()
g.start("close")
g.hold(5, 130)
g.start("precise", .3, 75)
