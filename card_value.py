def value_of_card(card):
    '''
    This function converts cards to integers and returns integers so they can be added
    Face cards are interpreted as 10
    '''

    # dictionary of cards and values
    # aces handled outside of function
    deck = {} 

    # make sure card is valid member of a 52-card deck
    assert card in deck.keys(), "Not a valid card"

    # extract card value from dictionary
    card_value = deck[card]

    return card_value
