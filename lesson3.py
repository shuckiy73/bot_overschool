import telebot
from telebot import types

bot = telebot.TeleBot("your token", parse_mode='HTML')


# @bot.message_handler(content_types=['sticker'])
# def handle_docs_audio(message):
# 	bot.reply_to(message, 'Стикер')
#
#
# @bot.message_handler(content_types=['text'])
# def handle_docs_audio(message):
# 	bot.reply_to(message, 'Текст')
#
#
# @bot.message_handler(content_types=['photo'])
# def handle_docs_audio(message):
# 	bot.reply_to(message, 'Фото')


@bot.message_handler(commands=['start'])
def run2(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    button2 = types.InlineKeyboardButton(text="10 - 20", callback_data="1")
    button3 = types.InlineKeyboardButton(text="20 - 40", callback_data="2")
    button4 = types.InlineKeyboardButton(text="Больше 40", callback_data="3")
    keyboard.add(button1)
    keyboard.row(button2, button3, button4)
    bot.send_message(message.chat.id, f'Сколько тебе лет?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == '1')
def callback_1(call):
    bot.send_message(call.message.chat.id, 'Тебе от <b>10</b> до <b>20</b> лет')


@bot.callback_query_handler(func=lambda call: call.data == '2')
def callback_2(call):
    bot.send_message(call.message.chat.id, 'Тебе от <b>20</b> до <b>40</b> лет')


@bot.callback_query_handler(func=lambda call: call.data == '3')
def callback_3(call):
    bot.send_message(call.message.chat.id, 'Тебе больше <b>40</b> лет')


@bot.message_handler(commands=['phone'])
def get_phone(message):
    keyboard = types.ReplyKeyboardMarkup()
    button_phone = types.KeyboardButton(text="Отправить номер", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Спасибо, мы с вами свяжемся', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def handle_docs_audio(message):
    print(message.contact.phone_number)


bot.infinity_polling()
