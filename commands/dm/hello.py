from lib.telegram_wrapper import *

# text = update["message"]["text"]

def command(t, update, args):
    chat = update["message"]["chat"]["id"]
    sent_from = update["message"]["from"]
    t.send_message("Hello "+sent_from["first_name"], chat)