#!/usr/bin/env python
# -*- coding: utf8 -*-

#This is the SoudQuest audio treasure hunt game for the Johnson County Library.
#An original idea by Maker in Residence Laura Spencer, Local Arts Journalist at KCUR
#Complete tutorial at [COMING SOON]
#Original Arduino project at [COMING SOON]

#Links
#Johnson County Library - http://jocolibrary.org/
#Johnson County Library MakerSpace - https://www.jocolibrary.org/we-recommend/listen-local
#KCUR - http://kcur.org/
#Laura Spencer at KCUR - http://kcur.org/people/laura-spencer

#This project requires:
#-RPi.GPIO - https://pypi.python.org/pypi/RPi.GPIO
#- VLC-python bindings from https://github.com/oaubert/python-vlc

#Resources
#Raspberry Pi GPIO pins and Python - https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
#Playing sounds and using buttons in Raspberry Pi - https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview
#Detecting a button press through GPIO - http://www.raspberrywebserver.com/gpio/detecting-a-button-press-through-GPIO.html

#---Code begins below this line!---

import time
import RPi.GPIO as GPIO

#We set up the GPIO pins naming scheme as GPIO BCM
GPIO.setmode(GPIO.BCM)

#We setup pin 23 as a GPIO input
GPIO.setup(23,GPIO.IN)


#We create a list to store user input
input_sequence = []

while True:
    
    if (GPIO.input(23) == False): #If a button press is detected
        print("Button pressed") #We print a message to the user
        input_sequence.append(1)
        print(input_sequence)


    time.sleep(0.1) #We pause a moment to avoid repeat state changes

#We clean the GPIO states
GPIO.cleanup()
