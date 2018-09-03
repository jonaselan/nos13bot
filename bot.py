#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def welcome(bot, update):
    text = (
        "Seja bem vindo, arrombiudo!"
    )
    update.message.reply_text(text)

def bye(bot, update):
    text = (
        "Já vai tarde, {name}!"
    ).format(name=update.message.left_chat_member.full_name)
    update.message.reply_text(text)

def cry(bot, update):
    bot.send_photo(chat_id = update.message.chat_id,
                   photo = open('imgs/jonas_chorando.jpg', 'rb'),
                   caption = "aa!")

def consideration(bot, update):
    bot.send_audio(chat_id = update.message.chat_id,
                   audio = open('audios/consideracao.mp3', 'rb'))

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.environ['NOS13BOT'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # lista de comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ajuda", help))
    dp.add_handler(CommandHandler("chora", cry))
    dp.add_handler(CommandHandler("consideracao", consideration))

    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome
    ))
    dp.add_handler(MessageHandler(
        Filters.status_update.left_chat_member, bye
    ))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
