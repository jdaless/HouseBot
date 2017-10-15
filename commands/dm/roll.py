from lib.telegram_wrapper import *
import random

def resultString(result, mod):
    num = len(result)
    s = sum(result)

    if num <= 10:
        r = "\n".join("{0}".format(n) for n in result) + "\nResult: " + str(s)
    elif num <= 50:
        r = " ".join("{0}".format(n) for n in result) + "\nResult: " + str(s)
    else:
        r = "Result: " + str(s)

    if mod > 0:
        r = r + "+" + str(mod) + "=" + str(s+mod)
    elif mod < 0:
        r = r + str(mod) + "=" + str(s+mod)

    return r

def command(t, update, args):
    chat = update["message"]["chat"]["id"]
    num = int(args[0].split("d")[0])
    sides = args[0].split("d")[1]
    mod = 0
    if "+" in args[0]:
        mod = int(sides.split("+")[1])
        sides = sides.split("+")[0]
    elif "-" in args[0]:
        mod = 0 - int(sides.split("-")[1])
        sides = sides.split("-")[0]

    result = []

    for i in range(0, num):
        roll = random.choice(range(1, int(sides)+1))
        result.append(roll)

    if len(args) > 1:
        if args[1] == "quietly":
            s = sum(result)
            r = "Result: " + str(s+mod)
        elif args[1] == "loudly":
            s = sum(result)
            r = "\n".join("{0}".format(n) for n in result) + "\nResult: " + str(s)
            if mod > 0:
                r = r + "+" + str(mod) + "=" + str(s+mod)
            elif mod < 0:
                r = r + str(mod) + "=" + str(s+mod)
    else:
        r = resultString(result, mod)


    t.send_message(r, chat)