# coding: utf8
import telebot

mySlaveToken = 'your Bot token here'
bot = telebot.TeleBot(mySlaveToken)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    print('userId: ', message.chat.id, ' Имя: ', message.from_user.first_name, message.from_user.last_name)
    if message.text == '/start':
        bot.send_message(message.chat.id, "Я бот Александра. Привет {0}! Напиши мне что то".format(message.from_user.first_name + ' ' + message.from_user.last_name ))
    else:
        bot.send_message(message.chat.id, "Я пока мало что умею но со временем я смогу больше. Хорошего Вам дня!")


if __name__ == '__main__':
    bot.polling(none_stop=True)
