from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Minimal camera settings
camera.resolution=(960,720)
#camera.framerate = 5 # frames/sec, determines the max shutter speed

#camera.exposure_mode = 'off'
#camera.shutter_speed = 500000 # exposure time in microsecs

#camera.awb_mode = 'off'
#camera.awb_gains = [1,1]

#camera.rotation = 90

# alpha window transparency 
#alpha =0
#camera.start_preview(alpha =200)

# Set ISO to the desired value
camera.iso = 600
# Wait for the automatic gain control to settle
sleep(5)

# Query shutter speed value
e = camera.exposure_speed
# Now fix the ss
camera.exposure_mode = 'off'
camera.shutter_speed = e
print('Shutter Speed: ' + str(e))

# Query awb gains
g = camera.awb_gains
# Now fix the gains
camera.awb_mode = 'off'
camera.awb_gains = g
print('AWB gains ' + str(g))


#Start preview
camera.start_preview()
sleep(10)
#camera.capture('preview.jpg')
camera.capture('image.png', 'png')
e = camera.exposure_speed
print('Shutter Speed: ' + str(e))

g = camera.awb_gains
print('AWB gains ' + str(g))

camera.stop_preview()
