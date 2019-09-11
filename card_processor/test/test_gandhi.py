from card_processor.src.process_gandhi import CardProcessor

processor = CardProcessor("Gandhi")


card_text_1 = """1. British Indian Army Defends the Empire
                    Raj Con Mus Rev
                    Colonial occupation: Add up to 6 cubes total to any Cities and
                    Provinces (up to 3 from Out of Play, remainder from Available).
                    Local troops mutiny: Remove up to 5 Sepoys from the map,
                    no more than 2 per space: first 3 to Available, remainder to Out
                    of Play.
                    Background. The British Indian Army
                    was a sizeable military force mainly
                    composed of Indian soldiers and British
                    officers. Its primary duty was the defense of India, but it also sent significant
                    forces to the Western Front in WWI, and
                    the Mediterranean and Asian theaters in
                    WWII.l"""

card_text_2 = """13. Ottoman Collapse Creates a Vacuum
                    Mus Raj Con Rev
                    Muslim community in India agitates for independence: Shift
                    Unity –2 or add 1 Muslim State to any Muslim Province with
                    no Raj Control (if State placed, Troops there to any Cities).
                    Muslim community seeks unity within India: Shift Unity +2.
                    Move 3 pieces from Out of Play to Available.
                    Background. The end of World War I
                    brought an end to the Ottoman Empire,
                    once the largest and most powerful
                    Muslim empire in history. The last Ottoman Sultan was also the last Caliph,
                    or political ruler of all Muslims. In India,
                    some in the Muslim community supported the pan-Islamic aims of the Khilafat movement to return a Caliph to
                    power, while others looked inward in
                    support of secular, Indian nationalism.
                    Non-player Instructions.
                    T NP Raj. This Event is not effective (8.8.3) for NP Raj."""


def test_card_1():
    card = processor.process_card(card_text_1)
    assert card.title == "British Indian Army Defends the Empire"
    assert card.number == '1'
    assert card.first_faction == 'Raj'
    assert card.second_faction == 'Con'
    assert card.third_faction == 'Mus'
    assert card.fourth_faction == 'Rev'
    assert card.flavor == 'Colonial occupation'


def test_card_2():
    card = processor.process_card(card_text_2)
    assert card.title == "Ottoman Collapse Creates a Vacuum"
    assert card.number == '13'
    assert card.first_faction == 'Mus'
    assert card.second_faction == 'Raj'
    assert card.third_faction == 'Con'
    assert card.fourth_faction == 'Rev'
    assert card.flavor == 'Muslim community in India agitates for independence'
