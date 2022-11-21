import telebot

bot = telebot.TeleBot("5839761500:AAH9vml5l6b4sgybI02ydB0iGLCj1MYb4-M")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello again.\nYou have found us.\nEnter the code if you want to continue our game…", parse_mode="MarkDown")

@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "82504":
        bot.send_message(message.chat.id, "Go to...", parse_mode="MarkDown")
        photo = open("photoBotAishat.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else: 
        bot.send_message(message.chat.id, "You really thought you got it right? Try again.", parse_mode="MarkDown")

bot.polling(none_stop=True)
