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
from config import config
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


LIST_ID = None #list ID to add tasks to


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def add(bot, update, args):
    task = ' '.join(args)
    list_id = LIST_ID
    card_endpoint =  'https://api.trello.com/1/cards'
    query = {"name":task,"pos":"top","idList":list_id,"key":config['key'],"token":config['token']}
    card_post = requests.request("POST", card_endpoint, params=query).json()
    bot.send_message(chat_id=update.message.chat_id, text='Added the task [{}] to list'.format(task))

def tasks(bot, update):
    list_id = LIST_ID
    cards_endpoint = 'https://api.trello.com/1/lists/{}/cards?fields=id,name'.format(list_id)
    cards = requests.request("GET", cards_endpoint, params=config).json()
    tasks = []
    for card in cards:
        tasks.append(card['name'])
    all_cards = ', '.join(tasks)
    bot.send_message(chat_id=update.message.chat_id, text='Tasks: {}'.format(all_cards.encode('utf-8')))



def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config['teleToken'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("task", add, pass_args=True))
    dp.add_handler(CommandHandler("tasks",tasks))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

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
