#flavortown_bot
from lib.telegram_wrapper import *
import importlib

TOKEN = None
HOUSE_CHAT_ID = None
HOUSE_IDS = []

with open("private.txt") as keyFile:
    TOKEN = keyFile.readline()[0:45]
    HOUSE_CHAT_ID = keyFile.readline()[0:10]
    stop = False
    while not stop:
        line = keyFile.readline()
        if line != "":
            if line[0] != "#":
                HOUSE_IDS.append(int(line[0:9]))
        elif line == "":
            stop = True

t = Telegram(TOKEN, HOUSE_CHAT_ID, HOUSE_IDS)

def parse_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            sent_from = update["message"]["from"]

            if str(chat) == HOUSE_CHAT_ID:
                if text.split()[0] == "bot,":
                    args = text.split()[1:]
                    com = importlib.import_module("commands.group."+args[0].lower())
                    if(len(args) > 1):
                        com.command(t, update, args[1:])
                    else:
                        com.command(t, update, None)
            elif str(chat) != HOUSE_CHAT_ID and sent_from["id"] in HOUSE_IDS:
                args = text.split()
                com = importlib.import_module("commands.dm."+args[0].lower())
                if(len(args) > 1):
                    com.command(t, update, args[1:])
                else:
                    com.command(t, update, None)
            else:
                t.send_message("You aren't part of the house, who are you?", chat)
        except Exception as e:
            print(e)
    

def main():
    last_update_id = None
    while True:
        updates = t.get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = t.get_last_update_id(updates) + 1
            parse_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()