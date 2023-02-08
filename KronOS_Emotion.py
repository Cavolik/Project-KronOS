#KronOS Emotion 1.2 Test Code
#TO DO: More quotes, Display face (animated?), Death, AI, Personality modules
import time
import configparser
from datetime import datetime
import os
import random
import requests
import calendar

time

city = 'nordfjordeid'
url = 'https://wttr.in/{}'.format(city)

config = configparser.ConfigParser()

likes = [5, 9, 17, 18, 20, 21, 22, 25, 31, 32, 39, 41, 50, 53, 55, 58, 61, 66, 67, 70, 71, 73, 75, 77, 78, 79, 80, 81, 82, 88, 89, 90]
dislikes = [4, 6, 7, 19, 23, 54, 63, 74, 83, 86, 91, 92]

#Match variable to entry in list
def match(element, lst):
  try:
    lst.index(element)
    #print("True")
    return True
  except ValueError:
    #print ("False")
    return False

song = "Null"
cal = calendar.TextCalendar()
#Quote lists
sleeping_list = ["ZZZ",
				 "*Computer noise*",
				 "No, Senpai! I love ... ZZZ"]
morning_list = ["Good mo...Wait, no its not!",
				"I dreamed that you were a dog.\nAnd the dog was my husband.\nAnyway, it was the worst dream ever.",
				"Did you oversleep again?\nUGH, you always keep me waiting!",]
regular_list = ["What are you looking at!?",
				"Ugh! You can be such a pain.",
				"You and I aren't friends or getting along together!",]
#Song Quotes				
likes_list = ["Hey, I realy like this song!\nWait, no! Forget I said anyting you baka!",
			  "Why do I have to be so embarrassed about the stuff I like?",
			  "Its not like I like this song or anything! B-baka!",
			  "I love this music, and I hate it at the same time.",]

dislikes_list = ["Seriously, Senpai. This song sucks.\nPlease let me play something better.",
				 "I'm sorry, but I have something called standards, you know.\n Please change the song.",
				 "I just realy hate this song, okay?"]
				
neutral_list = ["This song is kinda boring.",
				"Well, this is not the worst song I have heard, but also not the best.",
				"Don`t you have anything better to listen to?",]

time.sleep(11)

while True:
	#Get current song
	config.read('radio.ini')
	song_input = config["RADIO"]["playing"]
	if song_input.split(" ")[0] == "Internal":
		song_int = int(song_input.split(" ")[2])
	else:
		song_int = "Null"
	
	#Get current times
	time_now = datetime.now()
	H_now = time_now.hour
	M_now = time_now.minute
	
	if song != song_int:
		song = song_int
		#Sleeping
		sleeping_quote = sleeping_list[((random.randint(1,len(sleeping_list)))-1)]
		if 7 < H_now < 9:
			#Morning quotes
			regular_quote = morning_list[((random.randint(1,len(morning_list)))-1)]
		else:
			#Regular quotes
			regular_quote = regular_list[((random.randint(1,len(regular_list)))-1)]

		#Opinion on current song
		#if 
		if match(song, dislikes):
			song_quote = dislikes_list[((random.randint(1,len(dislikes_list)))-1)]

		elif match(song, likes):
			song_quote = likes_list[((random.randint(1,len(likes_list)))-1)]
		else:
			song_quote = neutral_list[((random.randint(1,len(neutral_list)))-1)]
		
		#Get weather
		res = requests.get(url)
		weather = res.text.split('\n')[2]
		w =''.join( '!'+x if 'A' <= x <= 'Z' else x for x in weather )
		weather_now = w.split('!')[1]
		
		
	#Talking stuff
	if 11 < H_now < 7:
		print (sleeping_quote)
	else:
		print (regular_quote)
	print (f"The time is {H_now}:{M_now}, you know.")
	print (f"I'm currently playing {song_input}.")
	print (song_quote)
	print ("Not that you would care, but here is the weather:")
	#Weather forecast
	for i in range(1,37):
		print (res.text.split('\n')[i])
		
	"""for i in range(2,7):
		print (res.text.split('\n')[i])"""

	print (weather_now)
	#print (cal.pryear(2023))
	time.sleep(0.06)
	#Clear screen
	os.system('cls' if os.name == 'nt' else 'clear')
