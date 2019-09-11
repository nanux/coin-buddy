from card_processor.src.process_gandhi import process_card

def test_line():
    card_text = """1. British Indian Army Defends the Empire
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
    
    card = process_card(card_text)

    assert card.title == "British Indian Army Defends the Empire"
    assert card.