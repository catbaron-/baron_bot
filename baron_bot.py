import logging, subprocess
from telegram.ext import Updater
from telegram.ext import CommandHandler

logging.basicConfig(format = '%(asctime)s - %(name)s - \
    %(levelname)s - %(messagename)s', level=logging.INFO)

TOKEN = ""
CMD = "/home/catbaron/script/proxy.sh|tail -1"
updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher

def func_start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
        text="23333, Big Brother Is Watching YOU.")
    bot.sendMessage(chat_id=update.message.chat_id,
        text="send /prx to update proxy server's ip")

def func_proxy(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
        text="Ok, I got it. Give me some minutes. \
I will let you know when I finish it.")
    update_cmd = CMD
    try:
        ip = subprocess.check_output(update_cmd, shell=True).decode('utf-8')
        bot.sendMessage(chat_id=update.message.chat_id,
            text="Server is updated as: {}".format(ip))
    except subprocess.CalledProcessError as e:
        err_msg = e.output
        bot.sendMessage(chat_id=update.message.chat_id,
            text="Error: {}".format(ip))

hdl_start = CommandHandler('start', func_start)
hdl_proxy = CommandHandler('prx', func_proxy)
dispatcher.add_handler(hdl_start)
dispatcher.add_handler(hdl_proxy)

updater.start_polling()
