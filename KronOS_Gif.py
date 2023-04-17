#KronOS GIF 1.0 Base code
#TODO: More gifs, Display face (animated?), Weather effect
import pygame
import os
import configparser
import requests
from datetime import datetime
from moviepy.editor import *

#Folder path GIF
dir_path = r'/home/raspberry/gifs 2'
gifs = os.listdir(dir_path)

likes = [5, 9, 17, 18, 20, 21, 22, 25, 31, 32, 39, 41, 50, 53, 55, 58, 61, 66, 67, 70, 71, 73, 75, 77, 78, 80, 81, 82, 89, 90]
dislikes = [4, 6, 7, 19, 23, 54, 63, 74, 83, 86, 91, 92]

config = configparser.ConfigParser()

city = 'nordfjordeid'
url = 'https://wttr.in/{}'.format(city)
#weather_now = "null"

pygame.display.set_caption('KronOS')

#Match variable to entry in list
def match(element, lst):
  try:
    lst.index(element)
    return True
  except ValueError:
    return False
    
def play_animation(anim):
	#Display animation 
	clip = VideoFileClip('/home/raspberry/gifs 2/' + anim + '.gif')
	clip.preview()
	
while True:
	#Get current song
	config.read('radio.ini')
	song_input = config["RADIO"]["playing_screen"]
	if song_input.split(" ")[0] == "Internal":
		song_int = int(song_input.split(" ")[2])
	else:
		song_int = "Null"
	song = song_int
	
	#Get current times
	time_now = datetime.now()
	H_now = time_now.hour
	M_now = time_now.minute
	
	#Get weather
	res = requests.get(url)
	weather = res.text.split('\n')[2]
	w =''.join( '!'+x if 'A' <= x <= 'Z' else x for x in weather )
	weather_now = w.split('!')[1]
	
	if H_now == 12 and M_now < 45:
		play_animation("food")
	
	elif match(song, likes):
		play_animation("useless")
		
	elif match(song, dislikes):
		play_animation("mad")
		
	elif weather_now == "Partly cloudy":
		play_animation("cloud")
		
	elif weather_now == "Sunny" or weather_now == "Clear":
		play_animation("sun")
		
	elif weather_now == "Rain" or weather_now == "Light rain":
		play_animation("rain")
	
	
	else:
		play_animation("error")
