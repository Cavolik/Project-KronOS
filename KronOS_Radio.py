#KronOS v1.7(List edition) Base Code
#TODO: Fix play/pause function, direct youtube download, fix HTTP connection error, add radio channels
import vlc
import random
import time
import RPi.GPIO as GPIO
import configparser
import os
from datetime import datetime

#Date
d = datetime.today()

#File path MP3
dir_path = r'/home/raspberry/musikkfolder'

#File for sharing data
config = configparser.ConfigParser()
config.read('radio.ini')

#Encoder pins
Enc_A = 25
Enc_B = 24
Button_A = 23
Button_B = 12

#Pinout setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_A, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Button_B, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Enc_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Enc_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Set up music player
def PlaySong(Input):
    global p
    p = vlc.MediaPlayer(Input)
    p.play()
    time.sleep(1)
    while p.is_playing():
        time.sleep(1)
    p.release()

PlaySong("/home/raspberry/musikkfolder/Boot.mp3")
time.sleep(5)

#MP3 links for radio stations
#Name displayed on screen before §, link to station after
stations = ["Internal Songs§sang",
            "NRK Nyheter§http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_h",
            "NRK Jazz§http://lyd.nrk.no/nrk_radio_jazz_mp3_h",
            "NRK Klassisk§http://lyd.nrk.no/nrk_radio_klassisk_mp3_h",
            "NRK Samisk§http://lyd.nrk.no/nrk_radio_sami_mp3_h",
            "NRK Folkemusikk§http://lyd.nrk.no/nrk_radio_folkemusikk_mp3_h",
            "NRK MP3§http://lyd.nrk.no/nrk_radio_mp3_mp3_h", 
            "NRK S&F§http://lyd.nrk.no/nrk_radio_p1_sogn_og_fjordane_mp3_h",
            "Radioparadise§http://stream-sd1.radioparadise.com:80/mp3-32",
            #"Country§http://www.frontiercountryonline.com",
            #"Elevator§http://113fm-atunwadigital.streamguys1.com/1010",
            "Irsk§http://solid24.streamupsolutions.com:8026/live",
            "Instrumental§http://igor.torontocast.com:2030/stream",
            "Disco§http://ruby.torontocast.com:1560/stream",
            "Dubstep§http://ice1.dubstep.fm/256mp3",
            "EPIC Rock§http://radio.streemlion.com:4200/stream",
            "USSR§http://s2.cdnradio.ru/ru-mp3-128",
            "Kinderradio§http://stream01.zogl.net:8906/stream",
            "Bollywood§http://ams1.reliastream.com:8046/live",
            "Texas Gospel§http://hazel.torontocast.com:1170/stream",
            #"Anime§http://audio.misproductions.com/japan128k",
            #"Vocaloid§http://vocaloidradio.com",
            "SEGA§http://content.radiosega.net:8006/rs-mpeg.mp3",
            "LO-FI§http://ec2.yesstreaming.net:1910/stream",
            "Dark Abiance§http://radio.m00.su:8001/darkambient.mp3",
            #"Alien§http://tantroniqradio.is-found.org:8000/tantroniq",
            #"Topp 40§https://s37.myradiostream.com/11662/listen.mp3"
            ]

#List of internal songs
IntList = os.listdir(dir_path)


JulList = ["/home/raspberry/musikkfolder/MariahCarey.mp3",#0
           "/home/raspberry/musikkfolder/ChristmasTime.mp3",#1
           "/home/raspberry/musikkfolder/Sarajevo.mp3",#2
           "/home/raspberry/musikkfolder/MinecraftFestive.mp3",#3
           "/home/raspberry/musikkfolder/ChristmastimeIsKillingUs.mp3",#4
           "/home/raspberry/musikkfolder/JingleBellRock.mp3",#5
           "/home/raspberry/musikkfolder/MagicalTime.mp3",#6
           "/home/raspberry/musikkfolder/1984.mp3",#7
           "/home/raspberry/musikkfolder/MetalChristmas.mp3",#8
           "/home/raspberry/musikkfolder/PadoruPadoru.mp3",#9
           "/home/raspberry/musikkfolder/CarolofTheBells.mp3",#10
           "/home/raspberry/musikkfolder/CarolofthebelsNC.mp3",#11
           "/home/raspberry/musikkfolder/CarolofTheBells.mp3",#12
           "/home/raspberry/musikkfolder/SantaTellMeNC.mp3",#13
           "/home/raspberry/musikkfolder/HeavyMetalChristmas.mp3",#14
           "/home/raspberry/musikkfolder/SilentNight.mp3",#15
           "/home/raspberry/musikkfolder/LittleDrummerBoy.mp3",#16
           "/home/raspberry/musikkfolder/JingleHell.mp3",#17
           "/home/raspberry/musikkfolder/DarkestCarols.mp3",#18
           "/home/raspberry/musikkfolder/Zone.mp3",#19
           "/home/raspberry/musikkfolder/WalkingintheAir.mp3",#20
           "/home/raspberry/musikkfolder/WinterWonderland.mp3",#21
           "/home/raspberry/musikkfolder/Rudolph.mp3",#22
           "/home/raspberry/musikkfolder/MerryLittleChristmas.mp3",#23
           "/home/raspberry/musikkfolder/ALotLikeChristmas.mp3",#24
           "/home/raspberry/musikkfolder/HollyJolly.mp3",#25
           "/home/raspberry/musikkfolder/ItsCold.mp3",#26
           "/home/raspberry/musikkfolder/DrivingHome.mp3",#27
           "/home/raspberry/musikkfolder/FelizNavidad.mp3",#28
           "/home/raspberry/musikkfolder/Songname.mp3",#29
           "/home/raspberry/musikkfolder/SleighRide.mp3",#30
           "/home/raspberry/musikkfolder/KillSanta.mp3",#31
           "/home/raspberry/musikkfolder/Cryptosanta.mp3"#32
           ]

#Set initial station number
station = 1
enc = 0
link = 0
LastState_A = GPIO.input(Enc_A)

#Get imput from rotary encoder
def rotation_decode(Enc_A):
    State_A = GPIO.input(Enc_A)
    State_B = GPIO.input(Enc_B)
    global LastState_A
    global enc
    if State_A != LastState_A:
        if State_B != State_A:
            enc += 1
            if enc > (len(stations)-1):
                enc = 0
        else:
            enc -= 1
            if enc < 0:
                enc = (len(stations)-1)
    LastState_A = State_A
    p.stop()
    time.sleep(0.01)
    
    return

GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)

#Play/pause music Curently not working
paused = False


def Button_A_active(Button_A):
    global paused
    if paused == True:
        p.set_pause(False)
        paused = False
        ##print("The music is playing")
    else:
        p.set_pause(True)
        paused = True
        ##print("The music has been paused")
    return

GPIO.add_event_detect(Button_A, GPIO.RISING, callback=Button_A_active, bouncetime=10)

#Skip current song
def Button_B_active(Button_B):
    p.stop()
    return

GPIO.add_event_detect(Button_B, GPIO.RISING, callback=Button_B_active, bouncetime=10)

#The actual code
while True:
    if station != enc:
        station = enc
    
    if enc == 0:
        if p.get_time() == p.get_length():
            #If Jul
            if datetime.today().month == 12:
                IntTimer = ((random.randint(1,len(JulList)))-1)
            
                playing = "Jul Song " + str(IntTimer)
                link = JulList[IntTimer]
                playing_ui = link.split('/')[4]
            #If not Jul
            else: 
                IntTimer = ((random.randint(1,len(IntList)))-1)
                
                playing = "Internal Song " + str(IntTimer)
                link = ("/home/raspberry/musikkfolder/" + IntList[IntTimer])
                playing_ui = link.split('/')[4]

            #Open file for sharing data
            fh = open("radio.ini", "w")
            config.set("RADIO", "playing_screen", playing)
            config.set("RADIO", "playing_ui", playing_ui)
            config.write(fh)
            fh.close()

            ##print(playing)
        ##else:
            ##print(p.get_time())
    else:
        playing = stations[station].split("§")[0]
        playing_ui = playing
        link = stations[station].split("§")[1]
        ##print("[%s]" % link)

        #Open file for sharing
        fh = open("radio.ini", "w")
        config.set("RADIO", "playing_screen", playing)
        config.set("RADIO", "playing_ui", playing_ui)
        config.write(fh)
        fh.close()

        ##print(playing)
    
    PlaySong(link)
    #Slight pause to debounce
    time.sleep(0.01)
