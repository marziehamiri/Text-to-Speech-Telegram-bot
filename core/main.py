import telebot
from gtts import gTTS
import os

os.environ["HTTP_PROXY"] = "http://127.0.0.1:12334"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:12334"

API_TOKEN = '9182263085:AAGFxwd4MY9_c2i0vhe9cQvehVwpTcHUAig'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"send me a text and I will read it for you")

@bot.message_handler(func=lambda message:True)
def texttospeech(message):
    text = message.text
    file_name = "output.mp3"
    output = gTTS(text=text,lang="en",tld="com.au")
    output.save(file_name)
    bot.send_voice(chat_id=message.chat.id,reply_to_message_id=message.id,voice=open(file_name,"rb"))
    os.remove(file_name)

bot.infinity_polling(skip_pending=True)

