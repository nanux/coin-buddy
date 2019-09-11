import re
import pprint
import json

card = None
cards = []
state = None

with open("games_unprocessed/falling_sky.txt", "r") as f:
    for line in f:
        # has title
        m = re.search("(\d+)\. (.*) (\w{2,3}) (\w{2,3}) (\w{2,3}) (\w{2,3})", line)
        if (m is not None):

            state = "title"
            
            if card is not None:
                cards.append(card)
                card = None

            card = {"number": m.group(1), "title": m.group(2),
            "first_faction": m.group(3), "second_faction": m.group(4),
            "third_faction": m.group(5), "fourth_faction": m.group(6)}

        m = re.search("CAPABILITY", line)
        if (m is not None):
            card["is_capability"] = True
            continue

        m = re.search("(Tip[s]?\.) (.*)", line)
        if (m is not None):
            state = "tips"
            card["tips"] = m.group(2)

        m = re.search("(Background.) (.*)", line)
        if (m is not None):
            state = "background"
            card["background"] = m.group(2)

        elif(state == "text"):
            m = re.search("^(.*)\: (.*)", line)
            if (m is not None):
                card["flavor_2"] = m.group(1)
                card["text_2"] = m.group(2)
                state = "text_2"
                continue

            line = line.rstrip('\n\r')
            card["text"] = f"{card['text']} {line}"
            continue

        elif(state == "text_2"):
            line = line.rstrip('\n\r')
            card["text_2"] = f"{card['text_2']} {line}"
            continue

        elif (state == "background"):
            line = line.rstrip('\n\r')
            card["background"] = f"{card['background']} {line}"
            continue

        elif (state == "tips"):
            line = line.rstrip('\n\r')
            card["tips"] = f"{card['tips']} {line}"
            continue

        m = re.search("^(.*)\: (.*)", line)
        if (m is not None):
            card["flavor"] = m.group(1)
            card["text"] = m.group(2)
            state = "text"

cards.append(card)

f = open('cards.json', 'w')
json.dump(cards, f, indent=4)
f.close()