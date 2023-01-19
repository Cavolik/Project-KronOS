#KronOS Clock 1.0 Base code
from datetime import datetime
import time
import configparser
import RPi.GPIO as GPIO

#Pinout setup
GPIO.setwarnings(False)
BUZZ_PIN = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ_PIN, GPIO.OUT)
GPIO.output(BUZZ_PIN,GPIO.LOW)

#File for sharing data
config = configparser.ConfigParser()
config.read('alarm.ini')

#Time format setup
now = datetime.now()
time_now = now.strftime("%H:%M:%S")
t_now = datetime.strptime(time_now, "%H:%M:%S")

#Alarms
ma = ["2;08:45:00", "1;10:15:00", "2;10:30:00", "1;12:00:00", "2;12:45:00", "1;14:15:00", "2;14:25:00", "3;15:55:00"]
ti = ["2;08:45:00", "1;10:15:00", "2;10:30:00", "1;12:00:00", "2;12:45:00", "3;14:15:00"]
on = ["2;08:45:00", "1;10:15:00", "2;10:30:00", "1;12:00:00", "2;12:45:00", "1;14:15:00", "2;14:25:00", "3;15:55:00"]
to = ["2;08:45:00", "1;10:15:00", "2;10:30:00", "1;12:00:00", "2;12:45:00", "1;14:15:00", "2;14:25:00", "3;15:10:00"]
fr = ["2;08:45:00", "1;10:15:00", "2;10:30:00", "1;12:00:00", "2;12:45:00", "3;14:15:00"]
lø = ["1;00:00:00", "1;01:00:00", "1;02:00:00", "1;03:00:00", "1;04:00:00", "1;05:00:00", "1;06:00:00", "1;07:00:00", "1;08:00:00", "1;09:00:00", "1;10:00:00", "1;11:00:00", "1;12:00:00", "1;13:00:00", "1;14:00:00", "1;15:00:00", "1;16:00:00", "1;17:00:00", "1;18:00:00", "1;19:00:00", "1;20:00:00", "1;21:00:00", "1;22:00:00", "3;23:00:00"]
sø = ["1;00:00:00", "1;01:00:00", "1;02:00:00", "1;03:00:00", "1;04:00:00", "1;05:00:00", "1;06:00:00", "1;07:00:00", "1;08:00:00", "1;09:00:00", "1;10:00:00", "1;11:00:00", "1;12:00:00", "1;13:00:00", "1;14:00:00", "1;15:00:00", "1;16:00:00", "1;17:00:00", "1;18:00:00", "1;19:00:00", "1;20:00:00", "1;21:00:00", "1;22:00:00", "3;23:00:00"]

#Days
li = [ma, ti, on, to, fr, lø, sø]
day = ["Mandag ", "Tirsdag", "Onsdag ", "Torsdag", "Fredag ", "Lørdag ", "Søndag "]

#Set day
a=now.weekday()

#Alarmfunction
def buzzNoise(num, paus):
    for i in range(num):
        GPIO.output(BUZZ_PIN,GPIO.HIGH)
        time.sleep(paus)
        GPIO.output(BUZZ_PIN,GPIO.LOW)
        time.sleep(paus)


while True:
    z = li[a]
    d = day[a]
    
    #Get time
    for i in range (len(z)):
        F = z[i].split(";")[1]
        alarm_type = z[i].split(";")[0]
        T = F.split(":")[0]
        M = F.split(":")[1]
        t_future = t_now.replace(hour=int(T), minute=int(M), second=0)
        time_future = t_future.strftime("%H:%M:%S")
        timeDiff = t_future-t_now
        now = datetime.now()
        time_now = now.strftime("%H:%M:%S")

        #Set clock
        while (time_now<time_future):
            now = datetime.now()
            time_now = now.strftime("%H:%M:%S")
            t_now = datetime.strptime(time_now, "%H:%M:%S")
            timeDiff = t_future-t_now

            #Transfer data to screen
            linje1 = d + " " + time_now
            linje2 = str(timeDiff) + " " + F
            fh = open("alarm.ini", "w")
            config.set("ALARM", "lin1", linje1)
            config.set("ALARM", "lin2", linje2)
            config.write(fh)
            fh.close()
            time.sleep(1)

        #Alarm
        if (time_now==time_future):
            if (alarm_type=="1"):
                #Friminut
                buzzNoise(2, 0.5)
            elif (alarm_type=="2"):
                #Time
                buzzNoise(1, 0.5)
            elif (alarm_type=="3"):
                #Slutt
                buzzNoise(1, 0.5)
                while (datetime.now().strftime("%p")=="PM"):
                    now = datetime.now()
                    time_now = now.strftime("%H:%M:%S")
                    time.sleep(1)
                now = datetime.now()
                a=now.weekday()
                z = li[a]
                d = day[a]
    i = 0
