import cv
import datetime
import time
import commands
from subprocess import call
from time import sleep
import RPi.GPIO as GPIO
 
# ---------------------------
# Setup the webcam and font
# ---------------------------

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
 
# define image size
imageWidth = 320
imageHeight = 240
 
# create a window object
cv.NamedWindow("window1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
 
# create a camera object
capture = cv.CaptureFromCAM(camera_index)
 
# set capture width and height
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_WIDTH, imageWidth );
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_HEIGHT, imageHeight );
 
# create a font
font = cv.InitFont(cv.CV_FONT_HERSHEY_COMPLEX_SMALL , 0.5, 0.5, 0, 1, cv.CV_AA)
 
while True:
 
    # get image from webcam
    frame = cv.QueryFrame(capture)
 
    # -------------------------------------------
    # Draw the time stamp on a white background
    # -------------------------------------------  
    cv.Rectangle(frame, (0,0), (imageWidth, 15), (255,255,255),cv.CV_FILLED,8,0)
    # get the current date and time
    timeStampString = datetime.datetime.now().strftime("%A_%Y-%m-%d_%I:%M:%S_%p")
    # insert the date time in the image
    cv.PutText(frame, timeStampString, (10,10), font, (0,0,0))
 
    # -----------------------------
    # show the image on the screen
    # -----------------------------
    cv.ShowImage("window1", frame)
    cv.WaitKey(10)
    
        

    if GPIO.input(11) == GPIO.LOW:
        print "Saving image..."
        timeStampString = datetime.datetime.now().strftime("%A_%Y-%m-%d_%I:%M:%S_%p")
        cv.SaveImage(timeStampString +".jpg",frame)
        print "Save success."
        print "Uploading to Dropbox..."
        photofile = "Dropbox-Uploader/dropbox_uploader.sh upload %s.jpg /pic" % timeStampString
        call ([photofile], shell = True)
        print "Upload success."
        print "==========================="
        sleep(0.1)
    if GPIO.input(13) == GPIO.LOW:
        print "Exit"
        break


