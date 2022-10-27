import telebot
from telebot.handler_backends import BaseMiddleware
from telebot.handler_backends import CancelUpdate
import os
import logging
from simple_colors import *
import json

get_json = json.load(open("session.json"))
TOKEN = get_json["TOKEN"]

try:
  bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
  
  class Started():
    print(green("Azuxi Unix Inc | © Copyright 2022", "bold"))
    print(green("Name project   : Telegram Bot", "bold"))
    print(green("Version        : Beta 0.0.0", "bold"))
    print(green("Author         : Miftah Fauzan", "bold"))
    print(green("===   Enjoy with our project    ===", "bold"))
    print("\n")
  class Logging():
    print(f"{telebot.logger.setLevel(logging.INFO)}")
  
  
  @bot.message_handler(commands=['start'])
  def send_welcome(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, "Hello, welcome to Azuxi Ichigawa.\nPlease visit the menu to see the menu list\n\n\nI\'m simple bot made by Miftah Fauzan with Love ♥️")
  @bot.message_handler(commands=['sendvoice'])
  def send_voice(message):
    voice = open("database/yaho.mp3", "rb")
    bot.send_chat_action(message.chat.id, "record_audio")
    bot.send_voice(message.chat.id, voice)
  
  bot.infinity_polling(interval=0, timeout=20)
  Started()
  Logging()
except:
  print("An exception occurred")