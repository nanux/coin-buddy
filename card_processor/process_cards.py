import re


def process_card_text(card_text):
    # 5. Aerostats CTWG
    # COALITION CAPABILITIES
    # Eye in the Sky: Taliban March costs +1 extra Resource per Space,
    # including LoCs.
    # Bomb kites and weather: Taliban March flips 1 Active Guerrilla
    # Underground per card.
    # Lightweight cameras and radars could be carried aloft by tethered
    # balloons, to carry out constant surveillance of roads, passes, defiles
    # or unobservable ground near a Coalition base or fighting position.
    # (JIEDDO website)

    card = {}
    m = re.match("(\d{1,2}) (.*) (\w)(\w)(\w)(\w)", card_text)
    if m is not None:
        card['number'] = m.group(1)
        card['title'] = m.group(2)
        card['first_faction'] = m.group(3)

    return card


with open("resources/unprocessed/distant_plain.txt", "r") as f:
    card_text = ""
    cards = []
    for line in f:
        # has title
        m = re.search("^(\d{1,3})\. (.*) (\w)(\w)(\w)(\w)", line)
        if m is not None:
            print(process_card_text(card_text))
            card_text = line
            continue

        card_text += line
        

