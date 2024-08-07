import telebot

bot = telebot.TeleBot('7487046378:AAH0BRwl_9L-drYDK0qml8pP2VMF1MubMw8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет')

@bot.message_handler(commands=['предсказание'])
def main(message):
    bot.send_message(message.chat.id, "[вы сдадите егэ по информатике на 5](https://t.me/infa_vikusya)",
                     parse_mode='Markdown')

@bot.message_handler(commands=['опасайтесь'])
def main(message):
    bot.send_message(message.chat.id, "злых учителей")


@bot.message_handler(commands=['ваша судьба'])
def main(message):
    bot.send_message(message.chat.id, "[вы будущий миллионер, если подпишитесь на Вику](https://t.me/infa_vikusya)",
                     parse_mode='Markdown')


bot.infinity_polling()