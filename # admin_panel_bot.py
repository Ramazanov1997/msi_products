# admin_panel_bot.py
import telebot
from telebot import types
from config import TOKEN
from database import Database

bot = telebot.TeleBot(TOKEN)
db = Database()
db.create_tables()

ADMIN_USER_ID = 1

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id == ADMIN_USER_ID:
        admin_panel(message.chat.id)
    else:
        bot.send_message(message.chat.id, "You are not authorized to access the admin panel.")

def admin_panel(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = [
        types.KeyboardButton("Option 1"),
        types.KeyboardButton("Option 2"),
        # Add more buttons as needed
    ]
    keyboard.add(*buttons)
    bot.send_message(chat_id, "Admin Panel", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # Your logic to handle regular messages
    pass

if __name__ == "__main__":
    bot.polling(none_stop=True)
