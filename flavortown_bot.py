#flavortown_bot

import json 
import requests
import time
import urllib

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

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def send_message_formatted(text, chat_id, parse_mode):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, chat_id, parse_mode)
    get_url(url)

def parse_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            sent_from = update["message"]["from"]
            if str(chat) == HOUSE_CHAT_ID and text.split()[0] == "bot,":
                args = text.split()
                if args[1] == "spam":
                    message = "R"
                    for id in HOUSE_IDS:
                        message = message + "[E](tg://user?id="+str(id)+")"
                    message = message + "!"
                    send_message_formatted(message, chat, "Markdown")
            elif sent_from["id"] in HOUSE_IDS:
                print(str(text) + " " + str(chat))
                send_message("I'm not smart enough to handle dms yet", chat)
            else:
                send_message("You aren't part of the house, who are you?", chat)
        except Exception as e:
            print(e)
    

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            parse_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()