import telebot
from telebot import types
bot = telebot.TeleBot('7857356004:AAGNMpIUS-7vL5k_qNUwas_uWSL9HUC0_YQ')
user_data = {}
import random
def new_year(name, relation):
    return [
        f"С Новым годом, {name}! Пусть этот год принесет тебе много счастья и удачи. От {relation}.",
        f"С наступающим Новым годом, {name}! Желаю, чтобы все мечты сбывались. От {relation}."
    ]
def birthday(name, relation):
    return [
        f"С днём рождения, {name}! Желаю здоровья, счастья и исполнения всех желаний. От {relation}.",
        f"{name}, ты — наша опора. С тобой мир становится надежнее, теплее и уютнее. Пусть все складывается наилучшим образом и тебе всегда сопутствует удача! От {relation}.",
        f"{name}! Пусть твои глаза светятся от счастья и улыбка не сходит с лица. Больше поводов для радости, светлых дней и приятных впечатлений. Пусть все складывается наилучшим образом! От {relation}.",
        f"{name}! Пусть судьба будет к тебе благосклонна, а Вселенная слышит все твои запросы. Желаю тебе много сил и энергии, чтобы жить эту замечательную жизнь на всю катушку, и денег — чтобы ни в чем себе не отказывать. От {relation}.",
        f"{name}, развивай свои таланты и покоряй новые вершины. Пожелаю тебе, чтобы с лихвой хватало и сил, и времени, и внутреннего запала на все! От {relation}.",
        f"С днем рождения, {name}! Преданной любви, материального благополучия, карьерного роста, отменного здоровья! Пусть проблемы будут нипочем и во всем сопутствует успех. От {relation}.",
        f"{name}, желаю, чтобы жизнь радовала приятными сюрпризами, рядом всегда были те, кого ты любишь. Всего наилучшего и счастливого праздника! С днем рождения!!! От {relation}.",
        f"С днем рожденья, {name}! Пусть твои глаза улыбаются, сердце поет, а на душе будет тепло и спокойно. Чтобы все задуманное непременно исполнилось! От {relation}.",
        f"Поздравляю с днем рождения, {name}! Искренне желаю тебе огромного счастья, чтобы все желания стремительно шли к реализации, а мечты превращались в реальность. Никогда не опускай руки и смело смотри вперед, чтобы позитив никогда тебя не покидал, а близкие люди были всегда рядом. Конечно же, желаю здоровья, куда же без него в любое время, и чтобы всё в жизни получалось так, как ты захочешь. От {relation}.",
        f"С днем рождения, {name}! В этот прекрасный день хочется пожелать всего хорошего и побольше. Много здоровья тебе, любви и счастья в жизни. Пускай все мечты реализуются легко и просто. Желаю по жизни идти с солнечным настроением и искренней улыбкой, встречать верных друзей и хороших людей на пути. Жизнь пусть будет наполнена добром и счастьем! От {relation}.",
        f"{name}, c днем рождения! Желаю тебе здоровья, счастья, успехов во всех начинаниях и исполнения всех заветных желаний. Пусть каждый день будет насыщен яркими впечатлениями, незабываемыми моментами и приятными сюрпризами. Желаю тебе бодрости духа, крепости характера, удачи в делах и любви в сердце. С днем рождения! От {relation}.",
        f"Поздравляю с днём рождения, {name}! Пусть каждый день будет наполнен радостью. От {relation}."
    ]
def feb_23(name, relation):
    return [
        f"С 23 Февраля, {name}! Желаю мужества и успехов во всех начинаниях. От {relation}.",
        f"Поздравляю с 23 Февраля, {name}! Пусть всегда будет место для подвигов. От {relation}."
    ]
def march_8(name, relation):
    return [
        f"С 8 Марта, {name}! Пусть в твоей жизни всегда будет весна и радость. От {relation}.",
        f"{name}! В этот светлый весенний праздник хочется от всей души поздравить тебя с Международным женский днем и пожелать самых важных и бесценных вещей: здоровья, любви и простого человеческого счастья. Пусть дома всегда царит тепло и уют, пусть близкие и родные всегда будут рядом, пусть жизнь будет полна радости. От {relation}.",
        f"Дорогая, {name}, поздравляю тебя с Международным женским днем — 8 Марта! От всей души желаю оставаться такой же прекрасной, никогда не унывать, не болеть и быть счастливой! Пусть все вокруг радует тебя, вдохновляет и наполняет энергией. Верь в себя и свои силы и знай, что ты достойна самого лучшего! От {relation}. ",
        f"С наступающим 8 Марта, дорогая {name}! Желаю, чтобы твои мечты всегда сбывались, а сердце было наполнено любовью и счастьем. От {relation}.",
        f"{name}, поздравляю с Международным женским днем! Надеюсь, что этот день станет началом новых и незабываемых впечатлений и приключений для тебя. Желаю тебе быть красивой, сильной и всегда уверенной в себе, а также всегда стремиться к новым вершинам. Пусть твоя жизнь будет наполнена любовью, заботой и теплом близких тебе людей. Желаю, чтобы каждый день приносил тебе радость и улыбки, а все твои мечты сбывались легко и быстро! От {relation}.",
        f"С Международным женским днем, {name}! Желаю любви и счастья в каждом дне. От {relation}."
    ]
def wedding(name, relation):
    return [
        f"Поздравляю с свадьбой, {name}! Желаю вам счастья и любви на долгие годы. От {relation}.",
        f"С днём вашей свадьбы, {name}! Пусть ваша жизнь будет полна радости и понимания. От {relation}."
    ]
def may_9(name, relation):
    return [
        f"С Днём Победы, {name}! Вечная память героям, защитившим нашу страну. От {relation}.",
        f"С 9 мая, {name}! Пусть мирное небо всегда будет над нами. От {relation}."
    ]
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введи имя человека, которого ты хочешь поздравить:')
    bot.register_next_step_handler(message, process_name_step)
def process_name_step(message):
    user_data[message.chat.id] = {'name': message.text}
    bot.send_message(message.chat.id, 'Теперь введи, кем ты ему являешься (например: друг, сестра и т.д.):')
    bot.register_next_step_handler(message, process_relation_step)
def process_relation_step(message):
    user_data[message.chat.id]['relation'] = message.text
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Новый год!', callback_data='new_year')
    btn2 = types.InlineKeyboardButton('День рождения!', callback_data='birthday')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('23 февраля!', callback_data='feb_23')
    btn4 = types.InlineKeyboardButton('8 марта!', callback_data='march_8')
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton('Свадьба!', callback_data='wedding')
    btn6 = types.InlineKeyboardButton('9 мая!', callback_data='may_9')
    markup.row(btn5, btn6)
    bot.send_message(message.chat.id, 'Выбери праздник:', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    holiday = call.data
    if call.message.chat.id in user_data:
        name = user_data[call.message.chat.id]['name']
        relation = user_data[call.message.chat.id]['relation']
        if holiday == 'new_year':
            messages = new_year(name, relation)
        elif holiday == 'birthday':
            messages = birthday(name, relation)
        elif holiday == 'feb_23':
            messages = feb_23(name, relation)
        elif holiday == 'march_8':
            messages = march_8(name, relation)
        elif holiday == 'wedding':
            messages = wedding(name, relation)
        elif holiday == 'may_9':
            messages = may_9(name, relation)
        # Выбираем случайное поздравление
        message_text = random.choice(messages)
        bot.send_message(call.message.chat.id, message_text)
bot.polling(none_stop=True)
