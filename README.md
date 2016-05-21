# CaptureToDropbox

## Device 
* Raspberry pi
* Button Switch
* USB WebCam

## How to do.
* install openCV
* git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
* Follow this http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi
* clone source code name "webCamButton.py"
* connect switch to raspberry pi
	- button switch input1 to GPIO11 use capture
	- button switch input2 to GPIO13 use close capture system
* run by sudo python webCamButton.py

## Fix Problem
* error: window system doesn't support openGL
	- apt-get update
	- apt-get install libgl1-mesa-dri
	- sudo reboot

* error: libv4l2 error setting pixformat device or resource busy
	- sudo fuser -k /dev/video0
