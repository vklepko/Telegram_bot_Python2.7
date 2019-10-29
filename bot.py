#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot;
import subprocess;

bot = telebot.TeleBot('835870103:AAGmS3Bt7aqD-dYuGeyhulCMQIOdb8BLLBw');

users = [376309226, 360548200]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.from_user.id in users:
		start(message)
	else:
		error(message)	

def start(message):
	data = message.text.split(" ", 2)
	if len(data) != 2:
		error(message)
	else:
		if data[1] == "younger":
			exec_command(data[0], "blacklist", message)
		elif data[1] == "older":
			exec_command(data[0], "blacklist1", message)
		else:
			error(message)	
		
def exec_command(num, table_name, message):
	MyOut = subprocess.Popen(['./block.sh', table_name, num], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
	stdout,stderr = MyOut.communicate()
	if stdout.find("Updated") != -1:
		bot.send_message(message.from_user.id, "Пользователь заблокирован.".decode('utf-8'))
	else:
		bot.send_message(message.from_user.id, "Ошибка, повторите попытку позже")

def error(message):
	bot.send_message(message.from_user.id, "пошел нахуй".decode('utf-8'))

bot.polling(none_stop=True, interval=0)

