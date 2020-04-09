# Written by Nathan
# Maybe one day you'll be able to drag the window around, but that's too much work
# place in the same directory as snip.exe - https://github.com/dlrudie/Snip/releases

import tkinter
import sys
import time
import threading

from tkinter import Tk, Message
from threading import Thread

window_height = '25'
window_width = '300'
horizontal_offset = '-1447'
verticle_offset = '1626'
conf_padding = 4
conf_font = 'consolas'
conf_font_size = 10
conf_font_width = 7
conf_update_frequency = 5

root = Tk()
root.title("Spotify Preview")
root.configure(background='#50505A')
root.attributes("-topmost", True)
root.overrideredirect(1)

spotify_info = Message(root, text='Nothing is playing', aspect=999999999, anchor='w')
spotify_info.config(font=(conf_font, conf_font_size,), background='#50505A', foreground='#F5F5FF')
spotify_info.pack(fill='both', expand=1, padx=conf_padding, ipadx=0, side='left')

def update_song():
	while(1):
		file = open('Snip.txt', encoding='utf8')
		file_song = file.read()
		if file_song == "":
			spotify_info.config(text = 'No Song')
			window_width = str(round(len('No Song') * conf_font_width) + (conf_padding*2 + conf_font_width))
		else:
			spotify_info.config(text = file_song)
			window_width = str(round(len(file_song) * conf_font_width) + (conf_padding*2 + conf_font_width))
		root.geometry(window_width + 'x' + window_height + '+' + horizontal_offset + '+' + verticle_offset)
		file.close()
		time.sleep(conf_update_frequency)

thread = Thread(target = update_song)
thread.setDaemon(True)
thread.start()

root.mainloop()
