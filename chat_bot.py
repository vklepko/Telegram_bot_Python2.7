#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot;
import subprocess;

bot = telebot.TeleBot('835870103:AAGmS3Bt7aqD-dYuGeyhulCMQIOdb8BLLBw');
#376309226
users = [360548200, 627765802]
chats = [-1001261481840, -385797206]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.chat.id in chats and message.from_user.id in users:
		start(message)
	
def start(message):
	data = message.text.split(" ", 2)
	if len(data) != 2:
		error(message)
	else:
		if data[1] == "младший".decode('utf-8'):
			exec_command(data[0], "blacklist", message)
		elif data[1] == "старший".decode('utf-8'):
			exec_command(data[0], "blacklist1", message)
		else:
			error(message)

def exec_command(num, table_name, message):
	MyOut = subprocess.Popen(['./block.sh', table_name, num],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
	stdout,stderr = MyOut.communicate()
	if stdout.find("Updated") != -1:
		bot.send_message(message.chat.id, "Пользователь заблокирован.".decode('utf-8'))
	else:
		bot.send_message(message.chat.id, "Ошибка, повторите попытку позже".decode('utf-8'))

def error(message):
	bot.send_message(message.chat.id, "пошел нахуй".decode('utf-8'))

bot.polling(none_stop=True, interval=0)
