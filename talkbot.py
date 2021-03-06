# -*- coding: utf-8 -*-
"""talkbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17N-tE0KQ2vQlcB9DDxUsZE0tz9adi_K5
"""

#all imports
import speech_recognition as sr
import PyAudio
import pyttsx3

from chatterbot import ChatBot
bot = ChatBot('Chotu')

#load the algorithm
from chatterbot.trainers import ChatterBotCorpusTrainer

#set the trainer
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train('chatterbot.corpus.english')

engine = pyttsx3.init()

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
          print('listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
 except:     
    pass

#interaction part
while True:
  message = command
  if message=='Bye' or message == 'bye':
    reply='Nice Talking. See you later.'
    engine.say(reply)
    engine.runandWait()
    print('{} : {}'.format(bot.name,reply))
    break
  else:
    reply = bot.get_response(message)
    engine.say(reply)
    engine.runandWait()  
    print('{} : {}'.format(bot.name,reply))