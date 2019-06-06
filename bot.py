import telebot


mySlaveToken = '877949812:AAF1memBG6qplUprQZ3nmGORHtYWIdWQ7oQ'
#'id': 594280870, 'first_name': 'Алёна'
#'id': 508011894, 'first_name': 'Olga'
bot = telebot.TeleBot(mySlaveToken)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    print('userId: ', message.chat.id, ' Имя: ', message.from_user.first_name)
    bot.send_message(message.chat.id, "Я бот Александра. Привет {0}!".format(message.from_user.first_name))


if __name__ == '__main__':
    bot.polling(none_stop=True)