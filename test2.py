import telebot

bot = telebot.TeleBot("8121194143:AAG8iBrkjbnKQyv1ogxDjji_Y1TNJ5ojecw")

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"{message.text}")
	
bot.polling()