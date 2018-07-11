from picamera import PiCamera
from time import sleep

camera = PiCamera()


# Minimal camera settings
camera.resolution=(960,720)
#camera.ISO=700
#camera.framerate = 1 # frames/sec, determines the max shutter speed
#camera.shutter_speed = 500000 # exposure time in microsecs
#camera.exposure_mode = 'off' #
#camera.awb_gains = [1,1]
#camera.awb_mode = 'off'
#camera.rotation = 90

# alpha window transparency 
#alpha =0
#camera.start_preview(alpha =200)

#Start preview
camera.start_preview()
sleep(10)
camera.stop_preview()
