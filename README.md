# edt

For our Industrial Cadets Gold Award Project we decided to create a prototype of a post-disaster robot that could detect humans, called the Hills Rover.
This repository contains the code that we used to make our robot move, run the camera and detect heat signatures.

Components:

Raspberry Pi Zero w https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/

Adafruit AMG8833 IR sensor https://shop.pimoroni.com/products/adafruit-amg8833-ir-thermal-camera-breakout?variant=984585994250

Waveshare motor driver PiHat https://www.waveshare.com/motor-driver-hat.htm

Libraries can be found in the requirements.txt file.

We programmed the IR sensor to upload data to a csv file, which is read by our website hosted locally on Flask.
This makes it easy to view the heatmap produced on any device connected to the same network as the Pi. 
