import telebot
from telebot import types
bot = telebot.TeleBot('7857356004:AAGNMpIUS-7vL5k_qNUwas_uWSL9HUC0_YQ')
user_data = {}
def new_year(name, relation):
    return [
        f"С Новым годом, {name}! Пусть этот год принесет тебе много счастья и удачи. От {relation}.",
        f"С наступающим Новым годом, {name}! Желаю, чтобы все мечты сбывались. От {relation}."
    ]
def birthday(name, relation):
    return [
        f"С днём рождения, {name}! Желаю здоровья, счастья и исполнения всех желаний. От {relation}.",
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
