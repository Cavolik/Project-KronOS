#KronOS v1.6(Jule edition) Base Code
#TODO: Fix play/pause, add radio channels, add songs
import vlc
import random
import time
import RPi.GPIO as GPIO
import configparser
from datetime import datetime

#Date
d = datetime.today()

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
            #"Country§http://ais-edge49-nyc04.cdnstream.com/2123_128.mp3",
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
            #"Vocaloid§http://mikamp.com/mikamp",
            "SEGA§http://content.radiosega.net:8006/rs-mpeg.mp3",
            "LO-FI§http://ec2.yesstreaming.net:1910/stream",
            "Dark Abiance§http://radio.m00.su:8001/darkambient.mp3",
            #"Alien§http://tantroniqradio.is-found.org:8000/tantroniq"
            ]

#List of internal songs(Must have full filepath)
IntList = ["/home/raspberry/musikkfolder/intothenight.mp3",#0
           "/home/raspberry/musikkfolder/relaxandsleep.mp3",#1
           "/home/raspberry/musikkfolder/spiritblossom.mp3",#2
           "/home/raspberry/musikkfolder/thecradleofyoursoul.mp3",#3
           "/home/raspberry/musikkfolder/JOJO.mp3",#4"
           "/home/raspberry/musikkfolder/Rickroll.mp3",#5
           "/home/raspberry/musikkfolder/FightingGold.mp3",#6
           "/home/raspberry/musikkfolder/takeahint.mp3",#7
           "/home/raspberry/musikkfolder/Fire.mp3",#8
           "/home/raspberry/musikkfolder/Megalovania.mp3",#9
           "/home/raspberry/musikkfolder/Halloween.mp3",#10
           ##"/home/raspberry/musikkfolder/WhiteNoise.mp3",#11
           ##"/home/raspberry/musikkfolder/1HourRandom.mp3",#12
           "/home/raspberry/musikkfolder/SovietAnthem.mp3",#13
           "/home/raspberry/musikkfolder/1812Overture.mp3",#14
           "/home/raspberry/musikkfolder/PokemonIntro.mp3",#15
           "/home/raspberry/musikkfolder/Pokerap.mp3",#16
           "/home/raspberry/musikkfolder/CatShark.mp3",#17
           ##"/home/raspberry/musikkfolder/SmashorPass.mp3",#18
           "/home/raspberry/musikkfolder/CrabRave.mp3",#19
           "/home/raspberry/musikkfolder/Chika.mp3",#20
           "/home/raspberry/musikkfolder/DOOM.mp3",#21
           "/home/raspberry/musikkfolder/MetalGear.mp3",#22
           "/home/raspberry/musikkfolder/RUSHE.mp3",#23
           "/home/raspberry/musikkfolder/LavenderTown.mp3",#24
           "/home/raspberry/musikkfolder/DragonMaid.mp3",#25
           "/home/raspberry/musikkfolder/Internett.mp3",#26
           ##"/home/raspberry/musikkfolder/RelaxingRain.mp3",#27
           "/home/raspberry/musikkfolder/Halo.mp3",#28
           "/home/raspberry/musikkfolder/NyanCat.mp3",#29
           "/home/raspberry/musikkfolder/Skyrim.mp3",#30
           "/home/raspberry/musikkfolder/StillAlive.mp3",#31
           "/home/raspberry/musikkfolder/WantYouGone.mp3",#32
           "/home/raspberry/musikkfolder/BurytheLight.mp3",#33
           "/home/raspberry/musikkfolder/Resurrections.mp3",#34
           "/home/raspberry/musikkfolder/FireAndFlames.mp3",#35
           "/home/raspberry/musikkfolder/GTA.mp3",#36
           "/home/raspberry/musikkfolder/GasGasGas.mp3",#37
           "/home/raspberry/musikkfolder/Lifelight.mp3",#38
           "/home/raspberry/musikkfolder/Radio.mp3",#39
           "/home/raspberry/musikkfolder/Shuba.mp3",#40
           ##"/home/raspberry/musikkfolder/Discs.mp3",#41
           "/home/raspberry/musikkfolder/MiiTheme.mp3",#42
           "/home/raspberry/musikkfolder/IndianaJones.mp3",#43
           "/home/raspberry/musikkfolder/SongofStorms.mp3",#44
           "/home/raspberry/musikkfolder/GerudoValley.mp3",#45
           "/home/raspberry/musikkfolder/FairyFountain.mp3",#46
           "/home/raspberry/musikkfolder/CHAD.mp3",#47
           "/home/raspberry/musikkfolder/Rasputin.mp3",#48
           "/home/raspberry/musikkfolder/Dorime.mp3",#49
           "/home/raspberry/musikkfolder/BadApple.mp3",#50
           "/home/raspberry/musikkfolder/TreasureBox.mp3"
           "/home/raspberry/musikkfolder/WidePutin.mp3",#52
           "/home/raspberry/musikkfolder/DragosteaDinTei.mp3",#53
           "/home/raspberry/musikkfolder/Boombastic.mp3",#54
           "/home/raspberry/musikkfolder/TakeOnMiku.mp3",#55
           "/home/raspberry/musikkfolder/BOOM.mp3",#56
           "/home/raspberry/musikkfolder/HEY.mp3"#57
           "/home/raspberry/musikkfolder/LeekSpin.mp3",#58
           "/home/raspberry/musikkfolder/BelieveinYou.mp3",#59
           "/home/raspberry/musikkfolder/Be My Guest.mp3",#60
           "/home/raspberry/musikkfolder/Counting.mp3",#61
           "/home/raspberry/musikkfolder/DovregubbensHall.mp3",#62
           "/home/raspberry/musikkfolder/Evangelion.mp3",#63
           "/home/raspberry/musikkfolder/Gigachad Boss.mp3",#64
           "/home/raspberry/musikkfolder/IceCreamLoli.mp3",#65
           "/home/raspberry/musikkfolder/Miku.mp3",#66
           "/home/raspberry/musikkfolder/MikuSinging.mp3",#67
           "/home/raspberry/musikkfolder/Oops.mp3",#68
           "/home/raspberry/musikkfolder/Pingu Boss.mp3",#69
           "/home/raspberry/musikkfolder/Reflect.mp3",#70
           "/home/raspberry/musikkfolder/Suzume.mp3",#71
           "/home/raspberry/musikkfolder/TemplarsInRain.mp3",#72
           "/home/raspberry/musikkfolder/Vitality.mp3",#73
           "/home/raspberry/musikkfolder/CruelAngelsCalculator.mp3",#74
           "/home/raspberry/musikkfolder/SweetdreamsKahoot.mp3",#75
           "/home/raspberry/musikkfolder/TwinkleTwinkle.mp3",#76
           "/home/raspberry/musikkfolder/NeurosamaScary.mp3",#77
           "/home/raspberry/musikkfolder/NeurosamaBased.mp3",#78
           "/home/raspberry/musikkfolder/SenkoNoises.mp3",#79
           "/home/raspberry/musikkfolder/Hanaji.mp3"#80
           ]

JulList = ["/home/raspberry/musikkfolder/MariahCarey.mp3",#0
           "/home/raspberry/musikkfolder/ChristmasTime.mp3",#1
           "/home/raspberry/musikkfolder/Sarajevo.mp3",#2
           "/home/raspberry/musikkfolder/MinecraftFestive.mp3",#3
           "/home/raspberry/musikkfolder/ChristmastimeIsKillingUs.mp3",#4
           "/home/raspberry/musikkfolder/JingleBellRock.mp3",#5
           "/home/raspberry/musikkfolder/LASTCHRISTMAS.mp3",#6
           "/home/raspberry/musikkfolder/MagicalTime.mp3",#7
           "/home/raspberry/musikkfolder/1984.mp3",#8
           ##"/home/raspberry/musikkfolder/MetalChristmas.mp3"#9
           "/home/raspberry/musikkfolder/PadoruPadoru.mp3",#10
           "/home/raspberry/musikkfolder/CarolofTheBells.mp3",#11
           "/home/raspberry/musikkfolder/CarolofthebelsNC.mp3",#12
           "/home/raspberry/musikkfolder/CarolofTheBells.mp3",#13
           "/home/raspberry/musikkfolder/SantaTellMeNC.mp3",#14
           "/home/raspberry/musikkfolder/HevyMetalChristmas.mp3",#15
           "/home/raspberry/musikkfolder/SilentNight.mp3",#16
           "/home/raspberry/musikkfolder/LittleDrummerBoy.mp3",#17
           "/home/raspberry/musikkfolder/JingleHell.mp3",#18
           "/home/raspberry/musikkfolder/DarkestCarols.mp3",#19
           "/home/raspberry/musikkfolder/Zone.mp3",#20
           "/home/raspberry/musikkfolder/CarlWheezer.mp3",#21
           "/home/raspberry/musikkfolder/WalkingintheAir.mp3"#22
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
    if station != enc:
        station = enc
    
    if enc == 0:
        if p.get_time() == p.get_length():
            #If Jul
            if datetime.today().month == 12:
                IntTimer = ((random.randint(1,len(JulList)))-1)
            
                playing = "Jul Song " + str(IntTimer)
                link = JulList[IntTimer]
            #If not Jul
            else: 
                IntTimer = ((random.randint(1,len(IntList)))-1)
                
                playing = "Internal Song " + str(IntTimer)
                link = IntList[IntTimer]

            #Open file for sharing data
            fh = open("radio.ini", "w")
            config.set("RADIO", "playing", playing)
            config.write(fh)
            fh.close()

            print(playing)
        else:
            print(p.get_time())
    else:
        playing = stations[station].split("§")[0]
        link = stations[station].split("§")[1]
        print("[%s]" % link)

        #Open file for sharing
        fh = open("radio.ini", "w")
        config.set("RADIO", "playing", playing)
        config.write(fh)
        fh.close()

        print(playing)
    
    PlaySong(link)
    #Slight pause to debounce
    time.sleep(0.01)
