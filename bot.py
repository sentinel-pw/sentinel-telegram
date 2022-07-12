"""
Copyright © Raveesh Yadav 2021 - htts://github.com/Raveesh1505

Description:
Sentinel is a fully secure password managing Telegram bot.

Version: 1.0
"""

import os
from dotenv import load_dotenv, find_dotenv

# Telegram libraries
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# Programme modules
import utils.edit as edit
import utils.extraction as extraction
import utils.load as load


# Extracting sensitive details set as env variables  
load_dotenv(find_dotenv())
TOKEN = os.getenv('BOT_TOKEN')

# Setting up a bot client
updater = Updater(TOKEN, use_context=True)


def start(update: Update, context: CallbackContext):
    '''Function to print the first message when the bot is started'''

    update.message.reply_text("Welcome!!!")


def help(update: Update, context: CallbackContext):
    '''Function to print all the commands and details of the bot'''

    update.message.reply_text("Help command working!!!")


async def addPass(update: Update, context: CallbackContext):
    """
    This function will help user add a new password to the database.
    Confirmation will be asked from the user before proceeding towards
    registration process which consists of encrytion and addition of data.
    """

    await update.message.reply_text("Add command working!!!")


def getPass(update: Update, context: CallbackContext):
    """
    This function will extract all the passwords of the user
    and print them into a table in the channel.
    """

    update.message.reply_text("Get command working")


def deletePass(update: Update, context: CallbackContext):
    """
    This function will delete the record that user dosent
    wants. It willtake username and website as parameters
    and delete the matching record. 
    """

    update.message.reply_text("Delete command working!!!")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('add', addPass))
updater.dispatcher.add_handler(CommandHandler('get', getPass))
updater.dispatcher.add_handler(CommandHandler('delete', deletePass))


if __name__ == "__main__":
    updater.start_polling()