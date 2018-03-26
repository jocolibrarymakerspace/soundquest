#!/usr/bin/env python
# -*- coding: utf8 -*-

#This is the SoundQuest audio treasure hunt game for the Johnson County Library.
#Original idea by Maker in Residence Laura Spencer, Local Arts Journalist at KCUR
#Complete tutorial at [COMING SOON]

#Links
#Johnson County Library - http://jocolibrary.org/
#Johnson County Library MakerSpace - https://www.jocolibrary.org/we-recommend/listen-local
#KCUR - http://kcur.org/
#Laura Spencer at KCUR - http://kcur.org/people/laura-spencer

#This project requires:
#-RPi.GPIO - https://pypi.python.org/pypi/RPi.GPIO
#-VLC-python bindings from https://github.com/oaubert/python-vlc

#Resources
#-Raspberry Pi GPIO pins and Python - https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
#-Playing sounds and using buttons in Raspberry Pi - https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview
#-Detecting a button press through GPIO - http://www.raspberrywebserver.com/gpio/detecting-a-button-press-through-GPIO.html

#---Code begins below this line!---

#We import the GPIO module
import RPi.GPIO as GPIO

#We import the time module
import time

#We import the signal library
import signal

#We import the VLC python bindings library
import vlc

#We set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#We define the GPIO pins for each button
GPIO.setup(22,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)
GPIO.setup(26,GPIO.IN)

#We create an object of the VLC class
player = vlc.MediaPlayer()

#We define the VLC playlist
#Add as many tracks as you need, just make sure to respect the formatting and put in the correct path!
#We use implied continuation of the list to make it easier to read.
playlist = ['/home/pi/title.mp3',
            '/home/pi/hint01.mp3',
            '/home/pi/hint02.mp3',
            '/home/pi/hint03.mp3',
            '/home/pi/hint04.mp3',
            '/home/pi/hint05.mp3',
            '/home/pi/error.mp3',]

#Create variable to store user input
input_sequence = ()

# Welcome message
print "Welcome to the SOUNDQUEST"
print "Press Ctrl-C to stop the game."
player = vlc.MediaPlayer(playlist[0]) #We request the title track in the playlist
player.play() #We start playing the title track

# This loop keeps checking for RFID tags. If one is near it will get the UID.
while True:
        if (GPIO.input(22) == True):
            print("Button pressed - append 1") #We print a message to the user
            input_sequence.append(1) #We append user input to the list
            print(input_sequence) #We print the current state of input_sequence
            time.sleep(0.3) #We pause the program to avoid repeat presses

        elif (GPIO.input(23) == True):
            print("Button pressed - append 1") #We print a message to the user
            input_sequence.append(2) #We append user input to the list
            print(input_sequence) #We print the current state of input_sequence
            time.sleep(0.3) #We pause the program to avoid repeat presses

        if (GPIO.input(24) == True):
            print("Button pressed - append 1") #We print a message to the user
            input_sequence.append(3) #We append user input to the list
            print(input_sequence) #We print the current state of input_sequence
            time.sleep(0.3) #We pause the program to avoid repeat presses

        elif (GPIO.input(25) == True):
            print("Button pressed - append 1") #We print a message to the user
            input_sequence.append(4) #We append user input to the list
            print(input_sequence) #We print the current state of input_sequence
            time.sleep(0.3) #We pause the program to avoid repeat presses

        elif (GPIO.input(26) == True):
            #This is where we decide which hint to play!
            if input_sequence == 1234: #Change the uid values to match your RFID tags
                player.stop()   #We stop playing any other track that might be playing
                print("I'm playing hint 01!")  #We announce which track is about to be played
                player = vlc.MediaPlayer(playlist[1]) #We request the  track in the playlist list
                player.play() #We play the track

            #Sample additional track playing block follows - uncomment and modify accordingly.
            #Add as many blocks as you have tracks to play.
            #if input_sequence == XXXX: #Change the uid values to match your RFID tags
            #    player.stop()   #We stop playing any other track that might be playing
            #    print("I'm playing track XX!")  #We announce which track is about to be played
            #    player = vlc.MediaPlayer(playlist[X])   #We summon the corresponding track in the playlist list
            #    player.play() #We start playing the track we just loaded

            else:
                print("I don't think that's a hint") #We let the user know that the track is being played (And we don't try playing it from the top)
                player = vlc.MediaPlayer(playlist[6]) #We request the  track in the playlist list
                player.play() #We play the track

        #We reset the input and button sequences
        input_sequence = () #We change the value of justread to store the latest tag UID we read
        button_sequence = ()#We reset the button sequence.

#And we do it all over again!
