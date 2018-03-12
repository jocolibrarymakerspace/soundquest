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

#We import the VLC library
#import VLC

#We create a list to store user input
input_sequence = []

#We create a variable to process user input
button_sequence = ()

#Create lists to store and compare sequences
prev_sequence = ()

#We define the VLC playlist
#Add as many tracks as you need, just make sure to respect the formatting and put in the correct path!
#We use implied continuation of the list to make it easier to read.
##playlist = ['/home/pi/hint01.mp3',
##            '/home/pi/hint02.mp3',
##            '/home/pi/hint03.mp3',
##            '/home/pi/hint04.mp3'
##            '/home/pi/hint05.mp3'
##            ]

# Welcome message
print ("Welcome to the SOUNDQUEST")

# This loop keeps checking for RFID tags. If one is near it will get the UID.
while True:
    message = "\nType in the test sequence" #DEBUG - We define the message to the player
    message += "\nOptions include: 12345, 54321, 45123, 32154, 45321" #DEBUG - #We define available testing options
    message += "\nPress q anytime to leave " #DEBUG - #We define available testing options
    
    input_sequence.append(input(message)) #We append user input to the list

    button_sequence = ''.join(map(str, input_sequence)) #We turn the input_sequence list content into a button_sequence string for processing
    print(button_sequence) #We print the contents of button_sequence

    #We compare sequences to play hints!
    if button_sequence == ("12345"): #Change the uid values to match your RFID tags
        print("I'm playing hint 01!")  #We announce which track is about to be played
##        player.stop()   #We stop playing any other track that might be playing
##        player = vlc.MediaPlayer(playlist[0])   #We request the  track in the playlist list
##        player.play() #We start playing the track we just loaded

    elif button_sequence == ("54321"): #Change the uid values to match your RFID tags
        print("I'm playing hint 02!")  #We announce which track is about to be played
##        player.stop()   #We stop playing any other track that might be playing
##        player = vlc.MediaPlayer(playlist[1])   #We request the  track in the playlist list
##        player.play() #We start playing the track we just loaded

    elif button_sequence == ("45123"): #Change the uid values to match your RFID tags
        print("I'm playing hint 03!")  #We announce which track is about to be played
##        player.stop()   #We stop playing any other track that might be playing
##        player = vlc.MediaPlayer(playlist[2])   #We request the  track in the playlist list
##        player.play() #We start playing the track we just loaded

    elif button_sequence == ("32154"): #Change the uid values to match your RFID tags
        print("I'm playing hint 04!")  #We announce which track is about to be played
##        player.stop()   #We stop playing any other track that might be playing
##        player = vlc.MediaPlayer(playlist[3])   #We request the  track in the playlist list
##        player.play() #We start playing the track we just loaded

    elif button_sequence == ("45321"): #Change the uid values to match your RFID tags
        print("I'm playing hint 05!")  #We announce which track is about to be played
##        player.stop()   #We stop playing any other track that might be playing
##        player = vlc.MediaPlayer(playlist[4])   #We request the  track in the playlist list
##        player.play() #We start playing the track we just loaded

    elif button_sequence == ("q"):
        break
    
    else:
        print("I don't get it brah.")

    input_sequence = [] #We reset the contents of input_sequence
    button_sequence = () #We reset the contents of button_sequence
    
#    break #DEBUG - We stop the program

#    prev_sequence = button_sequence #We store the latest input sequence for later
#    print (prev_sequence) #DEBUG - We check that button_sequence has been stored correctly

#And we do it all over again!
