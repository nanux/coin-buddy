import re
import pprint
import json

card = None
cards = []
state = None

with open("resources/unprocessed/fire_in_the_lake.txt", "r") as f:
    for line in f:
        # has title
        m = re.search("^(\d{1,2})\. (.*) (\w)(\w)(\w)(\w) (\d{4})", line)
        if (m is not None):

            state = "title"

            if card is not None:
                cards.append(card)
                card = None

            card = {"number": m.group(1), "title": m.group(2),
                    "first_faction": m.group(3), "second_faction": m.group(4),
                    "third_faction": m.group(5), "fourth_faction": m.group(6),
                    "year": m.group(7)}
            continue

        m = re.search("(\w+) CAPABILITY", line)
        if (m is not None):
            card["is_capability"] = True
            card["capability_faction"] = m.group(1)
            continue

        m = re.search("MOMENTUM", line)
        if (m is not None):
            card["is_momentum"] = True
            continue

        m = re.search("(Tip[s]?\.) (.*)", line)
        if (m is not None):
            state = "tips"
            card["tips"] = m.group(2)

        m = re.search("(Background.) (.*)", line)
        if (m is not None):
            state = "background"
            card["background"] = m.group(2)

        m = re.search("^Non-player Instructions.", line)
        if (m is not None):
            state = "non_player"
            card['non_player'] = ""
            continue

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

        elif (state == "non_player"):
            line = line.rstrip('\n\r')
            card["non_player"] = f"{card['non_player']} {line}"
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
