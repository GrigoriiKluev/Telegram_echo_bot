from telegram import Bot, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler,Filters)
from echo.config import TG_TOKEN,TG_API_URL



def do_start(bot:Bot, update:Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привет, ответь чтонибудь"
    )

def do_echo(bot:Bot, update:Update):
    chat_id = update.message.chat_id
    text = "Ваш id = {}\n\n{}".format(chat_id, update.message.text )
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )

def main():
    bot = Bot(token=TG_TOKEN, base_url=TG_API_URL)
    updater = Updater(bot=bot)

    start_handler = CommandHandler(
        "start", do_start
    )
    message_handler= MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
