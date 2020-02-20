import telebot

import os

token = '1000373070:AAH3lZtw2Qe6fzlVgeIECCnO8kxCbSy3Aok'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['restart'])
def restart(message):
    #os.system("cd C:\\Users\\Administrator\\Desktop\\ScheduleBotTGv.0.0.1\\BOTBOTBOTBOTBOT")
    os.system("python bot.py")
    bot.send_message(message.chat.id, "Restarted!")

bot.polling()
