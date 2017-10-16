from lib.telegram_wrapper import *

def command(t, update, args):
    chat = update["message"]["chat"]["id"]
    t.send_message(" ".join(args), chat)