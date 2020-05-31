import logging
import time

import scrapper
import settings

from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 	#?настройка logging, указываем формат лога (время и дата события, имя файла в котором произошло событие, уровень важности события, сообщение  событии)
                    level=logging.INFO,  											#? уровень логирования INFO - для получения информационных сообщений уровня info, warnig и error
					filename='bot.log') 	



def welcome_message(bot, update):
    text_welcome_message = 'Приветствую! \nЭтот бот позволит тебе получать обновления с портала интерфакс https://www.e-disclosure.ru/ по интересующему параметру. Для этого необходимо ввести наименование компании (краткое, без ошибок). Например, для отслеживания последних новостей об АО "Газпром" достаточно ввести сообщение Газпром\n\nдля поддержки разработчиков и развития бота Вы можете оказать материальную помощь в виде перевода на карту'
    print(text_welcome_message)
    update.message.reply_text(text_welcome_message)


def talk_to_me(bot, update):
	user_text = "OK {}! Ищем инфу по записи {}. В настоящий момент бот работает в тестовом режиме и парсит с периодичностью 1 итерация за 60 секунд.".format(update.message.chat.first_name, update.message.text) #переменная в которой лежит сообщение пользователя, включаем шаблон сообщения бота, которое будет вовзвращаться пользователю, с именем пользователя
	logging.info("User: %s, Chat id: %s, Message: %s, First_name: %s", update.message.chat.username, 
              update.message.chat.id, update.message.text, update.message.chat.first_name)  # возврат данных в лог username, id чата, сообщение
	# print(update.message)  # update.message возвращает в консоль данные пользователя и сообщение
	update.message.reply_text(user_text) # отправление текста пользователя в чат с пользователем и в консоль

#? def send_dog_pict(bot, update):
#? 	dog_list = glob('img/*dog*.jp*g')
#? 	dog_pic = choice(dog_list)
#? 	bot.send_photo(chat_id=update.message.chat.id, photo=open(dog_pic, 'rb'))


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Bot started')
    dp = mybot.dispatcher
    
    dp.add_handler(CommandHandler('start', welcome_message))
    #? dp.add_handler(CommandHandler('dog', send_dog_pict))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # add_handler для MessageHandler, устанавливаем фильтр для текста и производим вызов функции talk_to_me. #!MessageHandler должен быть последним Hendler'ом
    mybot.start_polling()#проверка новых сообщений
    mybot.idle() #бот будет работать до принудительной установки


main()