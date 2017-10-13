from lib.telegram_wrapper import *

def command(t, update, args):
    message = "R"
    for id in t.HOUSE_IDS:
        message = message + "[E](tg://user?id="+str(id)+")"
    message = message + "!"
    t.send_message_formatted(message, chat, "Markdown")