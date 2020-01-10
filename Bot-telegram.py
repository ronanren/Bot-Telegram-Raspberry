#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging, requests, socket
import unicodedata

token = "token"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

MAIN = 0


def start(bot, update):
    reply_keyboard = [['Ip', 'Temp', 'Stop']]

    update.message.reply_text(
        'Hi!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return MAIN


def main(bot, update):
    user = update.message.from_user
    logger.info("Message of %s: %s", user.first_name, update.message.text)


    if update.message.text == "Ip":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        private = s.getsockname()[0]
        s.close()
        ip = requests.get('https://api.ipify.org').text
        message = "Public IP : " + str(ip) + "\nPrivate IP : " + str(private)
        update.message.reply_text(message)


    if update.message.text == "Temp":
        
        message = os.system("vcgencmd measure_temp")
        update.message.reply_text(message)

    if update.message.text == "Stop":
        user = update.message.from_user
        logger.info("User %s canceled the conversation.", user.first_name)
        update.message.reply_text('Bye!',
                                  reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END


    return MAIN



def stop(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)



updater = Updater(token)

dp = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
            MAIN: [RegexHandler('^(Ip|Temp|Stop)$', main)],
        },

    fallbacks=[CommandHandler('stop', stop)]
)

dp.add_handler(conv_handler)

dp.add_error_handler(error)

# Commencer le Bot
updater.start_polling()

updater.idle()

