#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'token'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Приветствую тебя, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/Emegas19')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'http://t.me/Egor_Belov_QA')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить')
			sti = open('dontknow.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)

bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods