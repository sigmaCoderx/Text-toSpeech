
import telebot
from telebot import TeleBot,types
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from telebot.util import user_link
from gtts import gTTS



bot = telebot.TeleBot("5557353111:AAHfUi4HJit8CrhXWyrK2JzNhKaiA_68_eI")

def button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Group',url="t.me/neuralg"),
    InlineKeyboardButton(text='Channel',url="t.me/neuralp"))
    return markup
    
@bot.message_handler(commands=['start'],chat_types=['private'])
def sendWelcome(message):
    user = message.from_user
    bot.send_message(message.chat.id,f'Hello {user_link(user)} how are you\nthis is text to speech bot.for more explanation click /help',parse_mode='HTML',reply_markup=button())

@bot.message_handler(commands=['help'],chat_types=['private'])
def howto_use(message):
    text = '''
 send me any text i will convert it to speech.
 this bot is build by @developerspage 
 please support us by sharing the bot to your friends or you can buy me a coffee:) '''
    bot.send_message(message.chat.id,text)
    
@bot.message_handler(func=lambda m: True)
def textTo_speech(msg):
      text = msg.text
      to_speech = gTTS(text=text,lang='en')
      to_speech.save('result.mp3')
      with open('result.mp3','rb')as file:
          bot.send_voice(msg.chat.id,voice=file,reply_to_message_id = msg.message_id,reply_markup=button())
          
bot.infinity_polling()
      
