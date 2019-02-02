#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging, requests
import unicodedata

token = "Token"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

MAIN = 0


def start(bot, update):
    reply_keyboard = [['Ip', 'Meteo', 'Stop']]

    update.message.reply_text(
        'Hi!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return MAIN


def main(bot, update):
    user = update.message.from_user
    logger.info("Message of %s: %s", user.first_name, update.message.text)


    if update.message.text == "Ip":
        ip = requests.get('https://api.ipify.org').text
        message = "The public IP address of Raspberry Pi is : " + str(ip)
        update.message.reply_text(message)


    if update.message.text == "Meteo":
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Rennes,fr&APPID=Token')
        data = r.json()
        temp = data['main']['temp']
        celsius = float(temp) - 273.15
        message = "Rennes : " + str(round(celsius)) + "°C"
        update.message.reply_text(message)

    if update.message.text == "Stop":
        user = update.message.from_user
        logger.info("User %s canceled the conversation.", user.first_name)
        update.message.reply_text('Bye! I hope we can talk again some day.',
                                  reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END


    return MAIN



def stop(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)



updater = Updater(token)

dp = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
            MAIN: [RegexHandler('^(Ip|Meteo|Stop)$', main)],
        },

    fallbacks=[CommandHandler('stop', stop)]
)

dp.add_handler(conv_handler)

dp.add_error_handler(error)

# Commencer le Bot
updater.start_polling()

updater.idle()

