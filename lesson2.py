import telebot

bot = telebot.TeleBot("7055950109:AAGwHKJyfBYUChynWRweTRAF9AK9xUAPH30", parse_mode='HTML')


@bot.message_handler(commands=['start'])
def run2(message):
    bot.reply_to(message, f'Бот стартовал')


@bot.message_handler(commands=['hello'])
def run2(message):
    bot.reply_to(message, f'Привет дорогой пользователь\n'
                          f'Твой id: <b>{message.from_user.id}</b>\n'
                          f'Твой ник: <b>@{message.from_user.username}</b>\n'
                          f'Твоё имя: <b>{message.from_user.full_name}</b>\n'
                 )


@bot.message_handler(func=lambda message: '1' in message.text)
def run(message):
    bot.reply_to(message, f'Ты написал нам: <i><b>{message.text}</b></i>')


@bot.message_handler(func=lambda message: '2' in message.text)
def run(message):
    bot.send_message(message.chat.id, f'Ты написал нам: <b>{message.text}</b>')


bot.infinity_polling()
