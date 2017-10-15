# HouseBot
A telegram bot for automating activities in a smart-ish home. 

## Current commands:

### Group Chat

` bot, say {args} `

Bot will repeat args said to it

` bot, spam `

Bot will tag everyone in the house

### DM

` hello `

Bot says hi back

` roll {num}d{sides} {style} `

Bot rolls dice and tells you the total. {num} is the number of dice to be rolled and {sides} is the number of sides on each die. {style} can be blank, "quietly" or "loudly". If left blank, the bot will tell you rolls based on the number of dice. Under ten and each die result is sent on a new line, under 50 each die result is printed inline, but over 50 only the result is sent. "quietly" mimics the last behavior while "loudly" mimics the first. 

` say {args} `

Bot will repeat args said to it

` who am I `

Bot will tell you your name

## Setup

To work, the bot needs to run in python3, and needs a private.txt file with the bot api key, the house's group chat id, and each member of the house's telegram user id in that order. 