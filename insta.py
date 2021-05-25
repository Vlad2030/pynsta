# Pynst 25/05/2021.

# Import libraries.
from pyrogram import Client
from config import *
import time
import sys

# Code.
with Client('spam1', api_id, api_hash) as app: # spam1 is name of session. you can rename as u like. 
	i = 1 # i = 30 sec. (etc. i = 120 is a hour)
	print(i, d, 'Started...')
	while i <= 10000: # Cycle.
		app.send_message(inst_chat_id_1, inst_text + inst_link) # Send message to 1 chat.
		i += 1
		print(i, d, cum,'1 chat', d) # Succsesful message.
		time.sleep(10) # Cooldown time.
		app.send_message(inst_chat_id_1, inst_text + inst_link) # Send message to 1 chat.
		i += 1
		print(i, d, cum, '1 chat', d) # Succsesful message.
		time.sleep(10) # Cooldown time.
		app.send_message(inst_chat_id_1, inst_text + inst_link) # Send message to 1 chat.
		i += 1
		print(i, d, cum, '1 chat', d) # Succsesful message.
		time.sleep(10) # Cooldown time.
		app.send_message(inst_chat_id_2, inst_text + inst_link1) # Send message to 2 chat.
		i += 1
		print(i, d, cum, '2 chat', d) # Succsesful message.
	else: # if i => 'your number'.
		print(cum, i,'times', d)
		sys.exit()

app.run() # App run. ¯\_(ツ)_/¯
