import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

fwdleft = 17
fwdright = 18

revleft = 22
revright = 23

motors = [fwdleft,fwdright,revleft,revright]

for item in motors:
	GPIO.setup(item, GPIO.OUT)

def forward(i):
	GPIO.output(fwdright, True)
	GPIO.output(fwdleft, True)
	time.sleep(i)
	GPIO.output(fwdright, False)
	GPIO.output(fwdleft, False)

def right(i):
	GPIO.output(revright, True)
	GPIO.output(fwdleft, True)
	time.sleep(i)
	GPIO.output(revright, False)
	GPIO.output(fwdleft, False)	

def left(i):
	GPIO.output(fwdright, True)
	GPIO.output(revleft, True)
	time.sleep(i)
	GPIO.output(fwdright, False)
	GPIO.output(revleft, False)

def reverse(i):
	GPIO.output(revleft, True)
	GPIO.output(revright, True)
	time.sleep(i)
	GPIO.output(revleft, False)
	GPIO.output(revright, False)
