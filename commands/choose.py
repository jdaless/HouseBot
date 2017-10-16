from lib.telegram_wrapper import *
import random

def command(t, update, args):
    chat = update["message"]["chat"]["id"]
    r = random.choice(args)

    t.send_message("I choose " + r, chat)