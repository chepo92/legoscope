from picamera import PiCamera
import RPi.GPIO as GPIO
blue=36
red=38
green=40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(blue,GPIO.LOW)
GPIO.output(red,GPIO.LOW)
GPIO.output(green,GPIO.LOW)

GPIO.cleanup()
