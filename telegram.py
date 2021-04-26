import telebot
from telebot import types, TeleBot
import emoji
import random

token = "1622294288:AAF5xi2PeAi83bGPBm4dBe40-s7BLvIax7U"
bot: TeleBot = telebot.TeleBot(token)
s = 0
c = [0, 0, 0, 0]
smail = ['\U0001F607', '\U0001F63B', '\U0001F44D', '\U0001F642', '\U0001F970', '\U0001F929', '\U0000263A', '\U0001F63A']


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет. Как тебя зовут?'+random.choice(smail))
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, '{name}. Рад тебя видеть. Давай расскажу, как со мной работать'
                                      'Сначала введи свои баллы ЕГЭ - это могут быть гипотетические, реальные или '
                                      'баллы за пробник, чтобы обновить баллы напиши "/new"  и введи новые баллы.'
                                      'В данном боте вы можете рассчитать шанс поступления в вуз '
                                      'узнать информацию о вузах, понять, что такое профориентация и где ее можно '
                                      'получить и много другое. Если вы не сдаете один из предметов, введите по нему'
                                      'минимальный балл по информатике - 44, а по физике -39'.format(name=message.text)
                     + random.choice(smail))
    a = bot.send_message(message.chat.id, 'Введи свой балл ЕГЭ по русскому языку')
    bot.register_next_step_handler(a, ball)


def ball(message):
    c[0] = int(message.text)
    a = bot.send_message(message.chat.id, random.choice(smail)+'Отлично. Введи свой балл ЕГЭ по профильной математике')
    bot.register_next_step_handler(a, ball1)


def ball1(message):
    c[1] = int(message.text)
    a = bot.send_message(message.chat.id, random.choice(smail)+'Хорошо. Введи свой балл ЕГЭ по информатике')
    bot.register_next_step_handler(a, ball2)


def ball2(message):
    c[2] = int(message.text)
    a = bot.send_message(message.chat.id, random.choice(smail)+'Класс. Введи свой балл ЕГЭ по физике')
    bot.register_next_step_handler(a, ball3)


def ball3(message):
    s = 0
    c[3] = int(message.text)
    for i in range(len(c)):
        s += int(c[i])
    bot.send_message(message.chat.id, random.choice(smail)+'Отлично. Сумма твоих баллов {name}. Введи "старт"'.format(name=s))


@bot.message_handler(commands=['new'])
def hello1(message):
    a = bot.send_message(message.chat.id, 'Введи свой балл ЕГЭ по русскому языку')
    bot.register_next_step_handler(a, ball7)


def ball7(message):
    c[0] = int(message.text)
    a = bot.send_message(message.chat.id, random.choice(smail)+'Отлично. Введи свой балл ЕГЭ по профильной математике')
    bot.register_next_step_handler(a, ball6)


def ball6(message):
    c[1] = int(message.text)
    a = bot.send_message(message.chat.id, random.choice(smail)+'Хорошо. Введи свой балл ЕГЭ по информатике')
    bot.register_next_step_handler(a, ball5)


def ball5(message):
    c[2] = int(message.text)
    a = bot.send_message(message.chat.id, random.choice(smail)+'Класс. Введи свой балл ЕГЭ по физике')
    bot.register_next_step_handler(a, ball4)


def ball4(message):
    s = 0
    c[3] = int(message.text)
    for i in range(len(c)):
        s += int(c[i])
    bot.send_message(message.chat.id, random.choice(smail)+'Отлично. Сумма твоих баллов {name}. Введи "старт"'.format(name=s))


@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == "старт":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(
            *[types.KeyboardButton(name) for name in ['Тест по профориентации', 'Что такое профориентация', 'Вузы',
                                                      'Правила приема в вузы 2021', 'Подсказка «Как выбрать вуз».']])
        bot.send_message(message.chat.id, 'Выберите действие'+random.choice(smail), reply_markup=keyboard)
    elif message.text == 'Вузы':
        otvet = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton("Вузы Хабаровского края", callback_data="hab")
        button2 = types.InlineKeyboardButton("Вузы Владивостока", callback_data='Vlad')
        otvet.add(button1, button2)
        bot.send_message(message.chat.id, "Выбирай" + random.choice(smail), reply_markup=otvet)
    elif message.text == 'Правила приема в вузы 2021':
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        data1 = open('правила1.txt', 'rt', encoding='utf8').read().strip('')
        data2 = open('правила2.txt', 'rt', encoding='utf8').read().strip('')
        bot.send_message(message.chat.id, text=data1, reply_markup=keyboard1)
        bot.send_message(message.chat.id, text=data2, reply_markup=keyboard1)
    elif message.text == 'Подсказка «Как выбрать вуз».':
        keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        data = open('подзказка.txt', 'rt', encoding='utf8').read().strip('')
        bot.send_message(message.chat.id, text=data, reply_markup=keyboard2)
    elif message.text == 'Что такое профориентация':
        prof = types.InlineKeyboardMarkup(row_width=1)
        a = open('Профориентация.txt', 'rt', encoding='utf8').read().strip('')
        button1 = types.InlineKeyboardButton("Функции профориентации", callback_data="function")
        button2 = types.InlineKeyboardButton("Причины выбора профессии", callback_data='pritch')
        button3 = types.InlineKeyboardButton("Направления профориентации", callback_data='napr')
        prof.add(button1, button2, button3)
        bot.send_message(message.chat.id, a, reply_markup=prof)
    elif message.text == 'Тест по профориентации':
        k1 = types.InlineKeyboardMarkup(row_width=1)
        sq = types.InlineKeyboardButton(text='Билет в будущее', url="https://bilet.worldskills.ru/tests")
        info = types.InlineKeyboardButton(text="Какую IT профессию выбрать ",
                                          url='https://www.profguide.io/test/who-are-you-it-professions.html?utm_source=admitad&admitad_uid=17ea4741e1db374a5e100c6f738b2b05')
        sq1 = types.InlineKeyboardButton(text='Тест по профориентации',
                                         url="https://proftest.netology.ru/test/?status=restarted")
        k1.add(info, sq, sq1)
        bot.send_message(message.chat.id, 'Вот нескольо вариантов тестов по прориентации', reply_markup=k1)
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю, введите "старт"'+'\U00002639')


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    global c
    if call.data == "mainmenu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="Вузы Хабаровского края", callback_data="hab")
        second_button = types.InlineKeyboardButton(text="Вузы Владивостока", callback_data="Vlad")
        keyboardmain.add(first_button, second_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выбирай"+random.choice(smail),
                              reply_markup=keyboardmain)
    elif call.data == "Vlad":
        keyboard10 = types.InlineKeyboardMarkup(row_width=2)
        rele1 = types.InlineKeyboardButton(text="ДВФУ", callback_data="gg")
        rele2 = types.InlineKeyboardButton(text="ВГУЭП", callback_data="7")
        rele3 = types.InlineKeyboardButton(text="МГУ им. адм. Г.И. Невельского ", callback_data="10")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard10.add(rele1, rele2, rele3, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text="Выбирай вуз о котором хочешь узнать информацию", reply_markup=keyboard10)
    if call.data == "hab":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="TОГУ", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="ДВГУПС", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="ХГУЭП", callback_data="3")
        backbutton = types.InlineKeyboardButton(text="КНаУГу", callback_data="4")
        backbutton1 = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3, backbutton, backbutton1)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text="Выбирай вуз о котором хочешь узнать информацию", reply_markup=keyboard)
    elif call.data == "1":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        togu = open('ТОГУ.txt', 'rt', encoding='utf8').read().strip('')
        switch_button = types.InlineKeyboardButton(text='Сайт ТОГУ', url="https://pnu.edu.ru/ru/applicant/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="12")
        keyboard3.add(info, switch_button, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text=togu, reply_markup=keyboard3)
    elif call.data == "12":
        keyboard4 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ТОГУ', url="https://pnu.edu.ru/ru/applicant/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="13")
        keyboard4.add(chans, switch_button, backbutton)
        ti = open('ТОГУ IT.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text= ti, reply_markup=keyboard4)
    elif call.data == "2":
        k = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        sq = types.InlineKeyboardButton(text='Сайт ДВГУПС', url="https://abiturient.dvgups.ru/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="14")
        a = open('ДВГУПС.txt', 'rt', encoding='utf8').read().strip('')
        k.add(info, sq, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text=a,reply_markup=k)
    elif call.data == "14":
        keyboard5 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ДВГУПС', url="https://abiturient.dvgups.ru/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="25")
        keyboard5.add(chans, switch_button, backbutton)
        b = open('IT ДВГУПС.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=b, reply_markup=keyboard5)
    elif call.data == "56":
        keyboard5 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ХГУЭП', url="http://www.ael.ru/abiturientu/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="67")
        keyboard5.add(chans, switch_button, backbutton)
        b = open('ХГУЭП-ит.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=b, reply_markup=keyboard5)
    elif call.data == "3":
        ke = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ХГУЭП', url="http://www.ael.ru/abiturientu/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="56")
        ke.add(info, switch_button, backbutton)
        data = open('ХГУЭП.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data, reply_markup=ke)
    elif call.data == "function":
        g = types.InlineKeyboardMarkup(row_width=1)
        data = open('Функции профориентации.txt', 'rt', encoding='utf8').read().strip('')
        button2 = types.InlineKeyboardButton("Причины выбора профессии", callback_data='pritch')
        button3 = types.InlineKeyboardButton("Направления профориентации", callback_data='napr')
        g.add(button2, button3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data, reply_markup=g)
    elif call.data == "pritch":
        y = types.InlineKeyboardMarkup(row_width=1)
        data = open('Причины.txt', 'rt', encoding='utf8').read().strip('')
        button3 = types.InlineKeyboardButton("Направления профориентации", callback_data='napr')
        button1 = types.InlineKeyboardButton("Функции профориентации", callback_data="function")
        y.add(button1, button3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data,
                              reply_markup=y)
    elif call.data == "napr":
        o = types.InlineKeyboardMarkup(row_width=1)
        data = open('Направления профориентации.txt', 'rt', encoding='utf8').read().strip('')
        button1 = types.InlineKeyboardButton("Функции профориентации", callback_data="function")
        button2 = types.InlineKeyboardButton("Причины выбора профессии", callback_data='pritch')
        o.add(button1, button2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data,
                              reply_markup=o)
    elif call.data == "13":
        q1 = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт ТОГУ', url="https://pnu.edu.ru/ru/applicant/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('Тогу направления.txt', 'rt', encoding='utf8').read().strip('')
        n = [[a for a in d.split(';')] for d in data.split('\n')]
        q1.add(backbutton, s)
        chans = []
        s1 = int(c[0]) + int(c[1])
        s2 = int(c[0]) + int(c[1]) + int(c[2])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans.append(t)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
        else:
            for i in range(len(n)):
                if i == 1 or i == 2 or i == 3:
                    if (s2 >= int(n[i][1])) and (s2 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s2 >= int(n[i][2])) and (s2 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s2 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
                else:
                    if (s1 >= int(n[i][1])) and (s1 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s1 >= int(n[i][2])) and (s1 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s1 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
    elif call.data == "25":
        q2 = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт ДВГУПС', url="https://abiturient.dvgups.ru/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('ДВГУПС направления.txt', 'rt', encoding='utf8').read().strip('')
        w = [[a for a in d.split(';')] for d in data.split('\n')]
        q2.add(s, backbutton)
        chans1 = []
        s1 = int(c[0]) + int(c[1])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans1.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans1.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans1.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans1.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans1.append(t)
            d = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q2)
        else:
            for i in range(len(w)):
                if (s1 >= int(w[i][1])) and (s1 <= int(w[i][2])):
                    a = w[i][0] + ' - шанс поступить есть, но ниже среднего'
                    chans1.append(a)
                elif (s1 >= int(w[i][2])) and (s1 <= int(w[i][3])):
                    a = w[i][0] + ' - шанс поступить средний'
                    chans1.append(a)
                elif s1 >= int(w[i][3]):
                    a = w[i][0] + ' - шанс поступить высокий'+random.choice(smail)
                    chans1.append(a)
            d = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q2)
    elif call.data == "35":
        keyboard41 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ХГУЭП', url="http://www.ael.ru/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="265")
        keyboard41.add(chans, switch_button, backbutton)
        ti = open('ХГУЭП-ит.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text= ti, reply_markup=keyboard41)
    elif call.data == "4":
        keyboard6 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        togu = open('КнАГТу.txt', 'rt', encoding='utf8').read().strip('')
        switch_button = types.InlineKeyboardButton(text='Сайт КнАГТу', url="https://knastu.ru/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="31")
        keyboard6.add(info, switch_button, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=togu, reply_markup=keyboard6)
    elif call.data == "31":
        keyboard4 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт КнАГТу', url="https://knastu.ru/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="255")
        keyboard4.add(chans, switch_button, backbutton)
        ti = open('КнАГТу-ит.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text= ti, reply_markup=keyboard4)
    elif call.data == "gg":
        k1 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        sq = types.InlineKeyboardButton(text='Сайт ДВФУ', url="https://www.dvfu.ru/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="32")
        a = open('ДВФУ.txt', 'rt', encoding='utf8').read().strip('')
        k1.add(info, sq, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text=a,reply_markup=k1)
    elif call.data == "32":
        keyboard11 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ДВФУ', url="https://www.dvfu.ru/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="250")
        keyboard11.add(chans, switch_button, backbutton)
        ti = open('ДВФУ-ит.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text= ti, reply_markup=keyboard11)
    elif call.data == "7":
        keyboard12 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        togu = open('ВГУЭС.txt', 'rt', encoding='utf8').read().strip('')
        switch_button = types.InlineKeyboardButton(text='Сайт ВГУЭС', url="https://www.vvsu.ru/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="33")
        keyboard12.add(info, switch_button, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text=togu, reply_markup=keyboard12)
    elif call.data == "33":
        keyboard13 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт ВГУЭС', url="https://www.vvsu.ru/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="100")
        keyboard13.add(chans, switch_button, backbutton)
        ti = open('ВГУЭС-ит.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text= ti, reply_markup=keyboard13)
    elif call.data == "10":
        keyboard14 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        togu = open('МГУ им. адм. Г.И. Невельского.txt', 'rt', encoding='utf8').read().strip('')
        switch_button = types.InlineKeyboardButton(text='Сайт МГУ им. адм. Г.И. Невельского', url="https://www.msun.ru/")
        info = types.InlineKeyboardButton(text="Информация об IT направлениях", callback_data="34")
        keyboard14.add(info, switch_button, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,
                              text=togu, reply_markup=keyboard14)
    elif call.data == "34":
        keyboard14 = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        switch_button = types.InlineKeyboardButton(text='Сайт МГУ им. адм. Г.И. Невельского', url="https://www.msun.ru/")
        chans = types.InlineKeyboardButton(text="Рассчитать шанс поступить", callback_data="300")
        keyboard14.add(chans, switch_button, backbutton)
        ti = open('МГУ им. адм. Г.И. Невельского-ит.txt', 'rt', encoding='utf8').read().strip('')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text= ti, reply_markup=keyboard14)
    elif call.data == '67':
        q3 = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт ХГУЭП', url="http://www.ael.ru/abiturientu/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('ХГУЭП направления.txt', 'rt', encoding='utf8').read().strip('')
        w = [[a for a in d.split(';')] for d in data.split('\n')]
        q3.add(s, backbutton)
        chans1 = []
        s1 = int(c[0]) + int(c[1])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans1.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans1.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans1.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans1.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans1.append(t)
            d = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q3)
        else:
            for i in range(len(w)):
                if (s1 >= int(w[i][1])) and (s1 <= int(w[i][2])):
                    a = w[i][0] + ' - шанс поступить есть, но ниже среднего'
                    chans1.append(a)
                elif (s1 >= int(w[i][2])) and (s1 <= int(w[i][3])):
                    a = w[i][0] + ' - шанс поступить средний'
                    chans1.append(a)
                elif s1 >= int(w[i][3]):
                    a = w[i][0] + ' - шанс поступить высокий' + random.choice(smail)
                    chans1.append(a)
            d = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q3)
    elif call.data == '255':
        p = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт КнАГТу', url="https://knastu.ru/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('КНАГТУ направления.txt', 'rt', encoding='utf8').read().strip('')
        w = [[a for a in d.split(';')] for d in data.split('\n')]
        p.add(s, backbutton)
        chans1 = []
        s1 = int(c[0]) + int(c[1])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans1.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans1.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans1.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans1.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans1.append(t)
            f = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f,
                                  reply_markup=p)
        else:
            for i in range(len(w)):
                if (s1 >= int(w[i][1])) and (s1 <= int(w[i][2])):
                    a = w[i][0] + ' - шанс поступить есть, но ниже среднего'
                    chans1.append(a)
                elif (s1 >= int(w[i][2])) and (s1 <= int(w[i][3])):
                    a = w[i][0] + ' - шанс поступить средний'
                    chans1.append(a)
                elif s1 >= int(w[i][3]):
                    a = w[i][0] + ' - шанс поступить высокий' + random.choice(smail)
                    chans1.append(a)
            f = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f,
                                  reply_markup=p)
    elif call.data == "13":
        q1 = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт ТОГУ', url="https://pnu.edu.ru/ru/applicant/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('Тогу направления.txt', 'rt', encoding='utf8').read().strip('')
        n = [[a for a in d.split(';')] for d in data.split('\n')]
        q1.add(backbutton, s)
        chans = []
        s1 = int(c[0]) + int(c[1])
        s2 = int(c[0]) + int(c[1]) + int(c[2])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans.append(t)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
        else:
            for i in range(len(n)):
                if i == 1 or i == 2 or i == 3:
                    if (s2 >= int(n[i][1])) and (s2 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s2 >= int(n[i][2])) and (s2 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s2 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
                else:
                    if (s1 >= int(n[i][1])) and (s1 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s1 >= int(n[i][2])) and (s1 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s1 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
    elif call.data == "250":
        q1 = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт ДВФУ', url="https://www.dvfu.ru/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('ДВФУ аправления.txt', 'rt', encoding='utf8').read().strip('')
        n = [[a for a in d.split(';')] for d in data.split('\n')]
        q1.add(backbutton, s)
        chans = []
        s1 = int(c[0]) + int(c[1])
        s2 = int(c[0]) + int(c[1]) + int(c[2])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans.append(t)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
        else:
            for i in range(len(n)):
                if i == 0 or i == 1 or i == 3:
                    if (s2 >= int(n[i][1])) and (s2 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s2 >= int(n[i][2])) and (s2 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s2 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
                else:
                    if (s1 >= int(n[i][1])) and (s1 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s1 >= int(n[i][2])) and (s1 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s1 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
    elif call.data == "100":
        q1 = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт ВГУЭС', url="https://www.vvsu.ru/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('Экономики и сервиса.txt', 'rt', encoding='utf8').read().strip('')
        n = [[a for a in d.split(';')] for d in data.split('\n')]
        q1.add(backbutton, s)
        chans = []
        s1 = int(c[0]) + int(c[1]) + int(c[3])
        s2 = int(c[0]) + int(c[1]) + int(c[2])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans.append(t)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
        else:
            for i in range(len(n)):
                if i == 0 or i == 1 or i == 3:
                    if (s2 >= int(n[i][1])) and (s2 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s2 >= int(n[i][2])) and (s2 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s2 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
                else:
                    if (s1 >= int(n[i][1])) and (s1 <= int(n[i][2])):
                        a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                        chans.append(a)
                    elif (s1 >= int(n[i][2])) and (s1 <= int(n[i][3])):
                        a = n[i][0] + ' - шанс поступить средний'
                        chans.append(a)
                    elif s1 >= int(n[i][3]):
                        a = n[i][0] + ' - шанс поступить высокий'
                        chans.append(a)
            d = '\n'.join(chans)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=d,
                                  reply_markup=q1)
    elif call.data == '300':
        p = types.InlineKeyboardMarkup(row_width=1)
        s = types.InlineKeyboardButton(text='Сайт КнАГТу', url="https://knastu.ru/")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        data = open('МГУ.txt', 'rt', encoding='utf8').read().strip('')
        w = [[a for a in d.split(';')] for d in data.split('\n')]
        p.add(s, backbutton)
        chans1 = []
        s1 = int(c[0]) + int(c[1])
        if int(c[2]) > int(c[3]):
            s1 += int(c[2])
        else:
            s1 += int(c[3])
        if (int(c[0]) < 40) or (int(c[1]) < 39) or (int(c[2]) < 44) or (int(c[3]) < 33):
            t = 'Недостаточно баллов для подачи документов'
            chans1.append(t)
            if int(c[0]) < 40:
                t = 'Не хватает баллов по русскому языку.'
                chans1.append(t)
            if int(c[1]) < 39:
                t = 'Не хватает баллов по математике.'
                chans1.append(t)
            if int(c[2]) < 44:
                t = 'Не хватает баллов по информатике.'
                chans1.append(t)
            if int(c[3]) < 39:
                t = 'Не хватает баллов по физикe.'
                chans1.append(t)
            f = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f,
                                  reply_markup=p)
        else:
            for i in range(len(w)):
                if (s1 >= int(w[i][1])) and (s1 <= int(w[i][2])):
                    a = w[i][0] + ' - шанс поступить есть, но ниже среднего'
                    chans1.append(a)
                elif (s1 >= int(w[i][2])) and (s1 <= int(w[i][3])):
                    a = w[i][0] + ' - шанс поступить средний'
                    chans1.append(a)
                elif s1 >= int(w[i][3]):
                    a = w[i][0] + ' - шанс поступить высокий' + random.choice(smail)
                    chans1.append(a)
            f = '\n'.join(chans1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f,
                                  reply_markup=p)


if __name__ == "__main__":
    bot.polling(none_stop=True)