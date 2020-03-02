import telebot
import random

bot = telebot.TeleBot("714490897:AAGOl1xRr3QhFPk7g6MuHbs3-EYGzAJMtxA")

@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(message.from_user.id, "Приветствую!\nЗадай мне вопрос и Великий ответит тебе!!!")
    bot.send_message(message.from_user.id, "В конце предложения обязательно не забудь поставить знак вопроса!!!!!!")

@bot.message_handler(content_types=['text'])
def press_mycard(message):
    try:
        f = open('logg.txt', 'a')
        f.write(str(message.from_user.id) + '\n')
        f.write(message.text + '\n')
        f.close()
    except Exception:
        f = open('logg.txt', 'a')
        f.write(str(message.from_user.id) + '\n')
        f.write('Смог положить бота' + '\n')
        f.close()
    try:
        if len(message.text) == 1:
            bot.send_message(message.from_user.id, "Нормальный вопрос задай!")
            f = open('logg.txt', 'a')
            f.write('Один символ' + '\n')
            f.close()
        elif message.text[-1] == '?':
            if random.randrange(1, 3, 1)==1:
                bot.send_voice(message.from_user.id, open('NO.ogg', 'rb'))
                f = open('logg.txt', 'a')
                f.write('NO' + '\n')
                f.close()
            else:
                bot.send_voice(message.from_user.id, open('YES.ogg', 'rb'))
                f = open('logg.txt', 'a')
                f.write('YES' + '\n')
                f.close()
        else:
            bot.send_message(message.from_user.id, "Ну тут я не смогу помочь\nЛучше спроси у меня что-нибудь")
            f = open('logg.txt', 'a')
            f.write('Не вопрос' + '\n')
            f.close()
    except Exception:
        bot.send_message(message.from_user.id, "Ох, на меня очень большая нагрузка\nЯ устал, пытаюсь восстановиться\nЗайди через минутку, пожалуйста")
        f = open('logg.txt', 'a')
        f.write('Сломал' + '\n')
        f.close()

bot.polling(none_stop=True)
