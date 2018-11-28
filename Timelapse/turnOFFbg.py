from picamera import PiCamera
import RPi.GPIO as GPIO
blue=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(blue,GPIO.LOW)

GPIO.cleanup()
