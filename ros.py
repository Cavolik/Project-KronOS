#Downgrade of KronoOS that only plays music
import vlc
import random
import time
import RPi.GPIO as GPIO
import os

#Path to music folder
dir_path = "/home/raspberry/musikkfolder"

#Encoder pins
Button_A = 23
Button_B = 12

#Pinout setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_A, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Button_B, GPIO.IN, GPIO.PUD_UP)


#Set up music player
def PlaySong(Input):
    global p
    p = vlc.MediaPlayer(Input)
    p.play()
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)
    p.release()

PlaySong(dir_path + "/" + "Boot.mp3")
time.sleep(1)

#List of internal songs
IntList = os.listdir(dir_path)

#Play/pause music
paused = False

def Button_A_active(Button_A):
    global paused
    if paused == True:
        p.set_pause(False)
        paused = False
        print("The music is playing")
    else:
        p.set_pause(True)
        paused = True
        print("The music has been paused")
    return

GPIO.add_event_detect(Button_A, GPIO.RISING, callback=Button_A_active, bouncetime=10)

#Skip current song
def Button_B_active(Button_B):
    p.stop()
    return

GPIO.add_event_detect(Button_B, GPIO.RISING, callback=Button_B_active, bouncetime=10)

#The actual code
while True:

    #Play internal song
    if p.get_time() == p.get_length():
        IntTimer = ((random.randint(1,len(IntList)))-1)

        playing = "Internal Song " + str(IntTimer)
        link = (dir_path + "/" + IntList[IntTimer])
        
        print(f"Playing {link.split('/')[4]}")
    else:
        print(p.get_time())
    
    PlaySong(link)
    #Slight pause to debounce
    time.sleep(0.01)
