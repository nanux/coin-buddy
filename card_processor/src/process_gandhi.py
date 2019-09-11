import re
import pprint
import json
import logging
import dataclasses


@dataclass
class Card:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_card(text):
        log.info("processing card")
        card = Card()
        card.title = "test title"
        return card
