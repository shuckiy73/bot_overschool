import telebot
from telebot import types
from postgres_client import save_phone_to_db

bot = telebot.TeleBot("your token", parse_mode='HTML')


@bot.message_handler(commands=['start'])
def run2(message):
    keyboard = types.ReplyKeyboardMarkup()
    button_phone = types.KeyboardButton(text="Отправить номер", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Спасибо, мы с вами свяжемся', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    name = message.contact.first_name
    phone = message.contact.phone_number
    tg_id = message.from_user.id
    username = message.from_user.username
    save_phone_to_db(tg_id, phone, name, username)


bot.infinity_polling()
