import telebot
import sqllite_client

bot = telebot.TeleBot("7055950109:AAGwHKJyfBYUChynWRweTRAF9AK9xUAPH30", parse_mode='HTML')


def send_all(msg_pattern):
    clients = sqllite_client.get_all_clients()
    conter = 0
    for client in clients:
        bot.send_message(client[0], f'{client[1] + ", " if client[1] is not None else ""}{msg_pattern}')
        conter += 1
        print(f'Прогресс: {conter} / {len(clients)}')


send_all('привет, у нас супер акция 2')
