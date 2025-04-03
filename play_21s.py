# play_blackjack

import card_value
import ace_value
import higher_card
import is_blackjack
import split_pairs

import random

class deck(self):
    '''
    Class definition for a deck of cards, with methods for dealing from the deck
    '''
    def __init__(self):
        self.deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] * 4

    def deal_cards(self,n):
        '''
        Deal n cards from deck
        '''
        assert len(self.deck) >= n, "Not enough cards in deck. Deck needs refreshing"

        # sample without replacement
        deal = random.sample(self.deck, n)

        # remove dealt cards
        for card in deal:
            self.deck.remove(card)
            
        return deal

    def refresh(self):
        self.deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] * 4
    
def main():

    # initial deal of 2 cards
    hand = deck.deal_cards(2)

    # evaluate all cards that are not ace in hand
    hand_value = sum([card_value(x) for x in hand] if x != 'A')

    # evaluate for ace
    if 'A' in hand:
        ace = ace_value(hand_value)
        hand_value += ace

    # not a very smart strategy
    # keep asking for hits as long as haven't reached 21
    while hand_value <= 21:
        hit = deck.deal_cards(1)
        hand.append(hit)

        if hit == 'A':
            hit_value = ace_value(hit)
        else:
            hit_value = card_value(hit)

        hand_value += hit_value

    # check if have 21
    if hand_value == 21:
        print("Lucky 21!")

    return hand, hand_value
    

if __name__ == "__main__":
    main()
