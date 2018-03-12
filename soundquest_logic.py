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

#We import the time module
import time

#We import the signal library
import signal

#Create variable to store user input
button_sequence = ()

#Create lists to store and compare sequences
prev_sequence = ()

# Welcome message
print ("Welcome to the SOUNDQUEST")

# This loop keeps checking for RFID tags. If one is near it will get the UID.
while True:
    message = "\nType in the test sequence" #DEBUG - We define the message to the player
    message += "\nOptions include: 12345, 54321, 45123, 32154, 45321" #DEBUG - #We define available testing options
    message += "\nPress q anytime to leave" #DEBUG - #We define available testing options
    
    button_sequence = input(message)
    print(button_sequence)

    #This is where we compare sequences to play hints!
    if button_sequence == ("12345"): #Change the uid values to match your RFID tags
        print("I'm playing hint 01!")  #We announce which track is about to be played

    elif button_sequence == ("54321"): #Change the uid values to match your RFID tags
        print("I'm playing hint 02!")  #We announce which track is about to be played

    elif button_sequence == ("45123"): #Change the uid values to match your RFID tags
        print("I'm playing hint 03!")  #We announce which track is about to be played

    elif button_sequence == ("32154"): #Change the uid values to match your RFID tags
        print("I'm playing hint 04!")  #We announce which track is about to be played
        
    elif button_sequence == ("45321"): #Change the uid values to match your RFID tags
        print("I'm playing hint 05!")  #We announce which track is about to be played

    elif button_sequence == ("q"):
        break
    
    else:
        print("I don't get it brah.")
              
    prev_sequence = button_sequence #We store the latest input sequence for later
#    print (prev_sequence) #DEBUG - We check that button_sequence has been stored correctly
    button_sequence = () #We reset the button sequence value
#    print(button_sequence)#DEBUG - We check that button_sequence is empty

#And we do it all over again!
