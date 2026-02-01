import telebot
from telebot import types

# Токен должен быть в начале
TOKEN = "8540450313:AAGFP70mdZQBe79ZUnRqRNWnA8fqS3mwvfY"
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру ВНУТРИ функции
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Создаем кнопки
    btn1 = types.KeyboardButton("🎲 Случайное число")
    btn2 = types.KeyboardButton("ℹ️ Помощь")
    btn3 = types.KeyboardButton("📞 Контакты")
    
    # Добавляем кнопки в клавиатуру
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработчик НАЖАТИЙ на кнопки
@bot.message_handler(content_types=['text'])
def handle_buttons(message):
    if message.text == "🎲 Случайное число":
        # Тут будет генерация числа
        bot.send_message(message.chat.id, "Показываю случайное число...")
    elif message.text == "ℹ️ Помощь":
        bot.send_message(message.chat.id, "Это помощь!")
    elif message.text == "📞 Контакты":
        bot.send_message(message.chat.id, "Контакты: ...")
    else:
        bot.send_message(message.chat.id, "Я не понимаю эту команду")

# Запуск бота
bot.polling()