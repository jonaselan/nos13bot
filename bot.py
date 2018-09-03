#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    bot.send_voice(chat_id = update.message.chat_id,
                   voice = open('audios/consideracao.mp3', 'rb'),
                   duration = 8)

def marijuana(bot, update):
    bot.send_voice(chat_id = update.message.chat_id,
                   voice = open('audios/maconha.mp3', 'rb'))   

def dont_know(bot, update):
    bot.send_voice(chat_id = update.message.chat_id,
                   voice = open('audios/sabia_nao.mp3', 'rb'))   

def blz(bot, update):
    bot.send_voice(chat_id = update.message.chat_id,
                   voice = open('audios/blz.mp3', 'rb'))   

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
    dp.add_handler(CommandHandler("maconha", marijuana))
    dp.add_handler(CommandHandler("blz", blz))
    dp.add_handler(CommandHandler("sabia_nao", dont_know))
    dp.add_handler(CommandHandler("chora", cry))
    dp.add_handler(CommandHandler("consideracao", consideration))

    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome
    ))
    dp.add_handler(MessageHandler(
        Filters.status_update.left_chat_member, bye
    ))
    
    dp.add_error_handler(error)
    
    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()
