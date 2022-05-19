from encodings import utf_8
from arcade import Sound
from click import command
import telebot
import random
from telebot import types
import qrcode
from gtts import gTTS

kia_bot = telebot.TeleBot("5310910885:AAEz17DqK4hc2m40h456ga0fLtxWWNaaJqw")

@kia_bot.message_handler(commands=['start'])
def send_welcome(message):
    kia_bot.reply_to(message, "Hi dear, welcome to Guess_Number Game. please send /help ")

@kia_bot.message_handler(commands=['help'])
def send_help(message):
    kia_bot.reply_to(message, "Send this keys to play with me: /start  ,  /help , /game , /age , /qrcod , /voice ,  /bye  .  ")

@kia_bot.message_handler(commands=['game'])
def send_number(message):
    kia_bot.reply_to(message, "Please enter a number between 1 & 100 :")
    r = random.randint(0, 100)

    @kia_bot.message_handler(func= lambda m: True)
    def echo(message):
        f_name = message.from_user.first_name
        l_name = message.from_user.last_name
        x = int(message.text)
        if x==r:
            kia_bot.reply_to(message,f"Congrajulation, *** {f_name}  {l_name} *** , You Win ✅ ❤ ")
            kia_bot.reply_to(message, " /help ")
        elif x<r:
            kia_bot.reply_to(message,"Go up⏫")
        elif x>r: 
            kia_bot.reply_to(message,"Go down⏬")


@kia_bot.message_handler(commands =['qrcod'])
def send_a(message):
    f_name = message.from_user.first_name
    kia_bot.reply_to(message,f"please enter the string to get the QRCODE")
    @kia_bot.message_handler(func= lambda m: True)
    def echo(message):
        qrtext = message.text
        qrpic = qrcode.make(qrtext)
        qrpic.save("qrpic.png")
        photo = open('qrpic.png', 'rb')
        kia_bot.send_photo(message.chat.id, photo)

@kia_bot.message_handler(commands =['age'])
def send_age(message):
    f_name = message.from_user.first_name
    kia_bot.reply_to(message,f"hello {f_name} Please enter your Birth Year:")
    @kia_bot.message_handler(func= lambda m: True)
    def echo(message):
        birth_year = int(message.text)
        your_age = 1401 - birth_year
        kia_bot.reply_to(message,f"My dear,*** {f_name} ***, You are {your_age} yaers old!")

@kia_bot.message_handler(commands=['voice'])
def send_text(message):
    f_name = message.from_user.first_name
    kia_bot.reply_to(message,f"Hi ' {f_name} ' Please Enter your message in English to hear it.")
    @kia_bot.message_handler(func=lambda m:True)
    def echo(message):
        sound_text =gTTS(message.text)
        sound_text.save('sound_text.mp3')
        voice=open('sound_text.mp3','rb')
        kia_bot.reply_to(message.chat.id,voice)
        

@kia_bot.message_handler(commands=['bye'])
def send_welcome(message):
    kia_bot.reply_to(message, "Come back soon💘✅ ")

# @kia_bot.message_handler(commands=['fal'])
# def send_message(message):
#     fal_list = ['به فنا خواهی رفت', 'به دیدار معشوق خواهی رفت', 'به سفر خواهی رفت']
#     fal = random.choice(fal_list)
#     kia_bot.reply_to(message, fal)


kia_bot.infinity_polling()



