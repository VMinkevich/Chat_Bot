import time
import telebot
from ML_model import get_data, get_prediction

bot = telebot.TeleBot('5935156430:AAHegM3szRsktyzOSCGbc4XkFPiYFd5pPlY')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет! Введи Тикер ')


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, 'Анализируем...')

    answer = get_prediction(get_data(message.text))
    bot.send_message(message.chat.id, answer)


    do_again(message)


def do_again(message):
    bot.send_message(message.chat.id, 'Предсказать еще цену какой-то акции?')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except ():
            time.sleep(5)