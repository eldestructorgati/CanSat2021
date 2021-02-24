másinfo en https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2
import time
import picamera
camera.start_preview()
camera.resolution = (1920,1272)
camera.annotate_text_size = 18
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "Las Rozas a 1km de altitud"
if altitud >12:
 for i in range(10000000000):
  sleep(5)
  camera.capture('/home/pi/Desktop/image.jpg') 
  camera.stop_preview() 
