import re
import pprint
import json
import logging
import re


class CardProcessor:
    def __init__(self, game):
        self.game = game
        logging.info("processing card")

    def process_card(self, text):
        card = Card()
        # process the title
        self.process_title_and_number(text, card)
        self.process_factions(text, card)
        self.process_flavor(text, card)

        return card

    def process_title_and_number(self, text, card):
        # process the title
        m = re.search(r'(\d{1,2})\. (.*)', text)

        if(m):
            card.title = m.group(2)
            card.number = m.group(1)
        else:
            logging.warning(
                "Cannot find title and/or number in this card: " + text)

    def process_factions(self, text, card):
        m = re.search(r'(\w{2,3}) (\w{2,3}) (\w{2,3}) (\w{2,3})', text)

        if (m):
            card.first_faction = m.group(1)
            card.second_faction = m.group(2)
            card.third_faction = m.group(3)
            card.fourth_faction = m.group(4)
        else:
            logging.warning("Cannot factions in this card: " + text)

    # TODO fix the test
    def process_flavor(self, text, card):
        m = re.search(r'(.*): (.*)', text)

        if (m):
            card.first_faction = m.group(1)
            card.flavor = "Colonial occupation"       
        else:
            logging.warning("Cannot factions in this card: " + text)


class Card:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
