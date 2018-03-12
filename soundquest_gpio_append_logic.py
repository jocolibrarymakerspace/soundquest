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

#We import the Pi GPIO module
import RPi.GPIO as GPIO

#We set up the GPIO pins to use GPIO BCM name scheme
GPIO.setmode(GPIO.BCM)

#We setup pin 22, 23, 24, 25, 26, 27 as GPIO input
GPIO.setup(22,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)
GPIO.setup(26,GPIO.IN)
GPIO.setup(27,GPIO.IN)

#We create a list to store user input
input_sequence = []

#We create a variable to process user input
button_sequence = ()

# Welcome message
print ("Welcome to the SOUNDQUEST")

while True:

    if (GPIO.input(22) == False): #If a button press is detected
        print("Button pressed - append 1") #We print a message to the user
        input_sequence.append(1)
        print(input_sequence)

    elif (GPIO.input(23) == False): #If a button press is detected
        print("Button pressed - append 2") #We print a message to the user
        input_sequence.append(2)
        print(input_sequence)

    elif (GPIO.input(24) == False): #If a button press is detected
        print("Button pressed - append 3") #We print a message to the user
        input_sequence.append(3)
        print(input_sequence)

    elif (GPIO.input(25) == False): #If a button press is detected
        print("Button pressed - append 4") #We print a message to the user
        input_sequence.append(4)
        print(input_sequence)
    
    elif (GPIO.input(26) == False): #If a button press is detected
        print("Button pressed - append 5") #We print a message to the user
        input_sequence.append(5)
        print(input_sequence)

    elif (GPIO.input(27) == False): #If a button press is detected
        print("Checking sequence") #We print a message to the user
        button_sequence = ''.join(map(str, input_sequence)) #We turn the input_sequence list content into a button_sequence string for processing
        print("The button sequence is" + button_sequence) #We print the converted input_sequence

        #We compare sequences to play hints below
        if button_sequence == ("12345"):
            print("I'm playing hint 01!")

        elif button_sequence == ("54321"): #Comparing values against button_sequence
            print("I'm playing hint 02!")  #We announce which track is about to be played

        elif button_sequence == ("45123"): #Comparing values against button_sequence
            print("I'm playing hint 03!")  #We announce which track is about to be played

        elif button_sequence == ("32154"): #Comparing values against button_sequence
            print("I'm playing hint 04!")  #We announce which track is about to be played
        
        elif button_sequence == ("45321"): #Comparing values against button_sequence
            print("I'm playing hint 05!")  #We announce which track is about to be played
        
time.sleep(0.1) #We pause a moment to avoid repeat state changes

#We clean the GPIO states
GPIO.cleanup()