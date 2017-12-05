from lib.telegram_wrapper import *
import random

def command(t, update, args):
    # Randomly order the list of participants
    givers = [i for i in t.HOUSE_IDS]
    random.shuffle(givers)

    #Add a second list, shifting by a 1
    length = len(givers)
    shift_amount = 1
    receivers = [i for i in givers]
    for i in range(0, length):
        receivers[(i + shift_amount) % length] = givers[i]

    for i in range(0, length):
        message = "Your number is " + str(t.HOUSE_IDS.index(givers[i]))
        message = message + "\nGive a gift to " + str(t.HOUSE_IDS.index(receivers[i]))
        message = message + "\nPlease announce your number to the group."
        t.send_message(message, givers[i])