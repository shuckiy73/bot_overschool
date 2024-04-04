# pip install pyTelegramBotAPI


import telebot

bot = telebot.TeleBot("your token", parser_mode=None)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f'Ты написал нам: {message.text}')


bot.infinity_polling()
