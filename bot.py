import telebot
import os

TOKEN = os.getenv("7510794567:AAFbj1L6CLk8lKwnqYJlAUanrKRdihGsh-4")  # Pobiera token z Koyeb

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Cześć! Jestem Twoim botem do sygnałów krypto. 🚀")

bot.polling()
