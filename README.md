# HouseBot
A telegram bot for automating activities in a smart-ish home.

There are two ways to interact with the bot, chatting with it on telegram and hitting its flask API. 

## Current commands:

### Group Chat

` bot, say {args} `

Bot will repeat args said to it

` bot, spam `

Bot will tag everyone in the house

### DM

` hello `

Bot says hi back

` say {args} `

Bot will repeat args said to it

## API

` {address}:5000/doorbell `

Bot will send a message to the group chat letting everyone know there is someone at the door.

## Setup

To work, the bot needs to run in python3, and needs a private.txt file with the bot api key, the house's group chat id, and each member of the house's telegram user id in that order. 