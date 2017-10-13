from telegram_wrapper import *

# text = update["message"]["text"]

def command(t, update, args):
	if args[0] == "am" and args[1] == "I":
	    chat = update["message"]["chat"]["id"]
	    sent_from = update["message"]["from"]
	    t.send_message("You are "+ sent_from["first_name"] + " " + sent_from["last_name"], chat)