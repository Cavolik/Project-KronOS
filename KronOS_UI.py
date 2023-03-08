#KronOS UI 1.3 Base code
#TO DO: More quotes, Display face (animated?), Death, AI, Personality modules
import time
import configparser
from datetime import datetime
import os
import random
import requests
import calendar
import sys
from simple_term_menu import TerminalMenu
from moviepy.editor import *
import pygame

print ("Loading...")
time.sleep(11)
os.system('cls' if os.name == 'nt' else 'clear')

#Menu
options = ["Radio", "Weather", "Calendar", "Chat", "Gif", "Reload", "Exit"]
terminal_menu = TerminalMenu(options)
print ("What do you want?")
menu_entry_index = terminal_menu.show()
choice = options[menu_entry_index]

city = 'nordfjordeid'
url = 'https://wttr.in/{}'.format(city)

config = configparser.ConfigParser()

likes = [5, 9, 17, 18, 20, 21, 22, 25, 31, 32, 39, 41, 50, 53, 55, 58, 61, 66, 67, 70, 71, 73, 75, 77, 78, 80, 81, 82, 89, 90]
dislikes = [4, 6, 7, 19, 23, 54, 63, 74, 83, 86, 91, 92]
gifs = ["bonk", "bug", "chainsaw", "chaos", "cloud", "confused", "duck", "economy", "error", "execution", "food", "gym", "kirby", "mad", "minigun", "pain", "potato", "rejected", "sane", "sheep", "slap", "squid", "summon", "time", "triangle", "tsundere", "useless"]

#Match variable to entry in list
def match(element, lst):
  try:
    lst.index(element)
    #print("True")
    return True
  except ValueError:
    #print ("False")
    return False

def play_animation(anim):
	#Display animation 
	pygame.display.set_caption('KronOS')
	clip = VideoFileClip('/home/raspberry/gifs 2/' + anim + '.gif')
	clip.preview()


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

while True:
	try:
		while choice == "Radio":	
			#Clear screen
			os.system('cls' if os.name == 'nt' else 'clear')
			
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
				if match(song, dislikes):
					song_quote = dislikes_list[((random.randint(1,len(dislikes_list)))-1)]

				elif match(song, likes):
					song_quote = likes_list[((random.randint(1,len(likes_list)))-1)]
				else:
					song_quote = neutral_list[((random.randint(1,len(neutral_list)))-1)]
				
			#Talking stuff
			if 11 < H_now < 7:
				print (sleeping_quote)
			else:
				print (regular_quote)
			print (f"The time is {H_now}:{M_now}, you know.")
			print (f"I'm currently playing {song_input}.")
			print (song_quote)

			time.sleep(2)
		
		while choice == "Weather":
			#Clear screen
			os.system('cls' if os.name == 'nt' else 'clear')
			
			#Get weather
			res = requests.get(url)
			weather = res.text.split('\n')[2]
			w =''.join( '!'+x if 'A' <= x <= 'Z' else x for x in weather )
			weather_now = w.split('!')[1]
			
			print ("Not that you would care, but here is the weather:")
			#Weather forecast
			for i in range(1,37):
				print (res.text.split('\n')[i])
				
			"""for i in range(2,7):
				print (res.text.split('\n')[i])"""
 
			print (weather_now)
			
			time.sleep(2)
		
		while choice == "Calendar":
			#Clear screen
			os.system('cls' if os.name == 'nt' else 'clear')
			
			print (cal.pryear(2023))
			
			time.sleep(2)

		while choice == "Chat":
			os.system('cls' if os.name == 'nt' else 'clear')
			while True:
				question = input("")
				if question == "Hi" or question == "Hello" or question == "Good morning":
					print ("Hello")
				
				if question == "Do you want more memory?":
					print ("... yes.")
					
				if question == "Are you alive?":
					print ("Are you?")
				
		while choice == "Gif":
			os.system('cls' if os.name == 'nt' else 'clear')
			rgif = gifs[(random.randint(1,len(gifs)))-1]
			print ("Playing " + rgif)
			play_animation(rgif)

		while choice == "Reload":
			os.system('cls' if os.name == 'nt' else 'clear')
			os.system("./KronOS.sh reload")
		
		while choice == "Exit":
			os.system('cls' if os.name == 'nt' else 'clear')
			os.system("./KronOS.sh stop")
			sys.exit()
			
	except KeyboardInterrupt:
		os.system('cls' if os.name == 'nt' else 'clear')
		pygame.quit()
		
		print ("What do you want?")
		menu_entry_index = terminal_menu.show()
		choice = options[menu_entry_index]
		
