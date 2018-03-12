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


#We import the GPIO module
import RPi.GPIO as GPIO

#We set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#We define the GPIO pins for each button
GPIO.setup(XX,GPIO.IN)
GPIO.setup(XX,GPIO.IN)
GPIO.setup(XX,GPIO.IN)
GPIO.setup(XX,GPIO.IN)
GPIO.setup(XX,GPIO.IN)
GPIO.setup(XX,GPIO.IN)

#We import the time module
import time

#We import the signal library
import signal

#We import the VLC python bindings library
import vlc

#We create an object of the VLC class
player = vlc.MediaPlayer()

#We define the VLC playlist
#Add as many tracks as you need, just make sure to respect the formatting and put in the correct path!
#We use implied continuation of the list to make it easier to read.
playlist = ['/home/pi/hint01.mp3',
            '/home/pi/hint02.mp3',
            '/home/pi/hint03.mp3',
            '/home/pi/hint04.mp3',
            '/home/pi/hint05.mp3',]

#Create variable to store user input
button_sequence = ()

#Create lists to store and compare sequences
prev_sequence = ()

# Welcome message
print "Welcome to the SOUNDQUEST"
print "Press Ctrl-C to stop the game."

# This loop keeps checking for RFID tags. If one is near it will get the UID.
while True:

#We detect whether the Main Big Button has been pressed or not. 
if GPIO.input(XX):
    #This is where we decide which hint to play!
    if button_sequence == XXXXX: #Change the uid values to match your RFID tags
            player.stop()   #We stop playing any other track that might be playing
            print("I'm playing hint XX!")  #We announce which track is about to be played
            #player = vlc.MediaPlayer(playlist[0])   #We request the  track in the playlist list
            #player.play() #We start playing the track we just loaded

            #Sample additional track playing block follows - uncomment and modify accordingly.
            #Add as many blocks as you have tracks to play.
            #elif (uid[0]) == XXX and (uid[1]) == XXX:
            #    player.stop()   #We stop playing any other track that might be playing
            #    print("I'm playing track XX!")  #We announce which track is about to be played
            #    player = vlc.MediaPlayer(playlist[X])   #We summon the corresponding track in the playlist list
            #    player.play() #We start playing the track we just loaded

            #We store the card's uid into the justread variable for comparing later
            prev_sequence = button_sequence #We change the value of justread to store the latest tag UID we read
            button_sequence = ()#We reset the button sequence.

    else:
        print("You're already playing sound hint!") #We let the user know that the track is being played (And we don't try playing it from the top)
        time.sleep(5) #If the same card is still on the reader, we take a 5 seconds break before polling for RFID again. This does not interrupt the track being played.

#And we do it all over again!
