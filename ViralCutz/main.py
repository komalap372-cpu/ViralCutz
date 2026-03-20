import telebot

# Your Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome to the ViralCutz Bot!')

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling()