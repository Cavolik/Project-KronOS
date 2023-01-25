#KronOS Emotion 1.0 Test Code
#TO DO: Likes/Dislikes, Display, Death, Weather import
import time
import configparser
from datetime import datetime
import os

config = configparser.ConfigParser()

likes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
dislikes = ["31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"]

#Match variable to entry in list
def match(x, y):
	for i in y:
		if i in x:
			return True


while True:
	config.read('radio.ini')
	
	song = config["RADIO"]["playing"]
	
	time_now = datetime.now()
	H_now = time_now.hour
	M_now = time_now.second

	print (time_now)
	print (song)
	
	#Energy level
	if 11 < H_now < 7:
		print ("Asleep")
	elif 7 < H_now < 9:
		print ("Tired")
	else:
		print ("Not tired")

	#Opinion on current song
	if match(song, dislikes):
		print ("Dislikes song")

	elif match(song, likes):
		print ("Likes song")
	
	time.sleep(0.1)
	#Clear screen
	os.system('cls' if os.name == 'nt' else 'clear')
