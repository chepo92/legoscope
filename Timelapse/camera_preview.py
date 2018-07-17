# Reference: http://picamera.readthedocs.io/en/release-1.10/index.html
from picamera import PiCamera
from time import sleep

# Create Camera instance 
camera = PiCamera()
# The Pi’s camera has three ports, the still port (for images), the video port (recording), and the preview port. 

# Minimal camera settings
camera.resolution=(960,720) 	# Retrieves or sets the resolution at which image captures, video recordings, and previews will be captured.
#camera.framerate = 5 # frames/sec, determines the max shutter speed

# Set ISO to the desired value
camera.iso = 600    # Retrieves or sets the apparent ISO setting of the camera.

# Wait for the automatic gain control to settle
sleep(5)

# Advanced camera users:
# -------------------------------------------------------------

# These are other possible parameters to change, depending on experiment:
#camera.analog_gain = 1  			# Retrieves the current analog gain of the camera.
#camera.awb_gains = [1,1] 			# Gets or sets the auto-white-balance gains of the camera. This attribute only has an effect when awb_mode is set to 'off'.
#camera.awb_mode = 'off'    		# Retrieves or sets the auto-white-balance mode of the camera.
#camera.brightness = 50				# Retrieves or sets the brightness setting of the camera.
#camera.color_effects=None			# Retrieves or sets the current color effect applied by the camera.
#camera.contrast = 0        		# useful to take reduce the background
#camera.digital_gain				# Retrieves the current digital gain of the camera.
#camera.exposure_compensation=0  	# Retrieves or sets the exposure compensation level of the camera.
#camera.exposure_mode = 'off'	 	# Retrieves or sets the exposure mode of the camera.
#camera.exposure_speed				# Retrieves the current shutter speed of the camera.
#camera.framerate = 0.01			# Retrieves or sets the framerate at which video-port based image captures, video recordings, and previews will run.
#camera.image_denoise				# Retrieves or sets whether denoise will be applied to image captures. Default true
#camera.image_effect='none'
#camera.image_effect_params
#camera.meter_mode
#camera.rotation = 90  				# Retrieves or sets the current rotation of the camera’s image.
#camera.saturation = 0  			# Retrieves or sets the saturation setting of the camera. 
#camera.sensor_mode					# Retrieves or sets the input mode of the camera’s sensor. setting this property does nothing unless the camera has been initialized with a sensor mode other than 0.
#camera.sharpness = 0 				# Retrieves or sets the sharpness setting of the camera. [-100, 100]
#camera.shutter_speed = 500000 		# Retrieves or sets the shutter speed of the camera in microseconds.

# alpha window transparency 
#alpha =0
#camera.start_preview(alpha =200)

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
# Any attempt to capture an image without using the video port will (temporarily) select the 2592x1944 mode while the capture is performed (this is what causes the flicker you sometimes see when a preview is running while a still image is captured).
camera.capture('image.png', 'png')  # use_video_port defaults to False which means that the camera’s image port is used. This port is slow but produces better quality pictures.
e = camera.exposure_speed
print('Shutter Speed: ' + str(e))

g = camera.awb_gains
print('AWB gains ' + str(g))

camera.stop_preview()

camera.close()

