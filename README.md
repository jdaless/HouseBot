# HouseBot
A telegram bot for automating activities in a smart-ish home.

There are two ways to interact with the bot, chatting with it on telegram and hitting its flask API. 

## Current commands:

### Group Chat

` bot, choose {args} `

Bot will choose one of the (space separated) args given to it. 

` bot, say {args} `

Bot will repeat args said to it

` bot, spam `

Bot will tag everyone in the house

### DM

` bot, choose {args} `

Bot will choose one of the (space separated) args given to it. 

` hello `

Bot says hi back

` roll {num}d{sides} {style} `

Bot rolls dice and tells you the total. {num} is the number of dice to be rolled and {sides} is the number of sides on each die. {style} can be blank, "quietly" or "loudly". If left blank, the bot will tell you rolls based on the number of dice. Under ten and each die result is sent on a new line, under 50 each die result is printed inline, but over 50 only the result is sent. "quietly" mimics the last behavior while "loudly" mimics the first. 

` say {args} `

Bot will repeat args said to it

` who am I `

Bot will tell you your name

## API

` {address}:5000/doorbell `

Bot will send a message to the group chat letting everyone know there is someone at the door.

## Setup

The following instructions are for Ubuntu Server 16.04
```bash
sudo apt-get install -Y python3 python-pip3 `
sudo -H pip3 install flask configparser
```

Create a telegram-housebot.conf following the example in telegram-housebot.conf.example. Be sure to include the Telegram api key, the house's group chat id, the server address, and each member of the house's telegram user id

```bash
./flavortown_bot.py
```
