import random

MIN_CARD_VALUE = 0
MAX_CARD_VALUE = 52
MAX_CARD_PER_SUIT = 13

NUM_PLAYERS = 2
MAX_HAND_SIZE = int((MAX_CARD_VALUE / NUM_PLAYERS))

DECK_SHUFFLE_CONSTANT = 7

HEARTS_SUIT_OFFSET = MIN_CARD_VALUE + (0 * MAX_CARD_PER_SUIT)
SPADES_SUIT_OFFSET = MIN_CARD_VALUE + (1 * MAX_CARD_PER_SUIT)
DIAMONDS_SUIT_OFFSET = MIN_CARD_VALUE + (2 * MAX_CARD_PER_SUIT)
CLUBS_SUIT_OFFSET = MIN_CARD_VALUE + (3 * MAX_CARD_PER_SUIT)

class Card(BaseException):

    #Adjust the card value to ignore suit
    def __init__ (self, value = 0):
        if (value >= CLUBS_SUIT_OFFSET):
            self.value = value - CLUBS_SUIT_OFFSET
        elif (value >= DIAMONDS_SUIT_OFFSET):
            self.value = value - DIAMONDS_SUIT_OFFSET
        elif (value >= SPADES_SUIT_OFFSET):
            self.value = value - SPADES_SUIT_OFFSET
        else:
            self.value = value

    def dump(self):
        print( self.__dict__ )

class Deck(BaseException):

    def __init__ (self):
        self.cards = []

        for cnt in range(MIN_CARD_VALUE, MAX_CARD_VALUE):
            self.cards.append( Card(cnt) )


    def shuffle(self):
        # Go through the Deck some tunable amount of times.
        for y in range(0, DECK_SHUFFLE_CONSTANT):
            for x in range(MIN_CARD_VALUE, MAX_CARD_VALUE):

                #determine a card to swap with cards[x]
                swap = random.randrange(MIN_CARD_VALUE, MAX_CARD_VALUE, 3)

                # swap the randomly picked cards
                tmpCard = self.cards[x]
                self.cards[x] = self.cards[swap]
                self.cards[swap] = tmpCard

    def deal(self, num):
        # return the first card on the list
            return (self.cards.pop(0) )

    def showDeck(self):
        for c in self.cards:
            c.dump()


class Hand(BaseException):

    def __init__(self):
        self.cards = []

    def seeCard(self):
        return ( self.cards[0] )

    def playCard(self):
        return ( self.cards.pop(0) )

    def cardsLeft(self):
        return len(self.cards)

    def shuffle(self):
        # Go through the Deck some tunable amount of times.
        for y in range(0, DECK_SHUFFLE_CONSTANT):
            for x in range(0, len(self.cards)):

                #determine a card to swap with cards[x]
                swap = random.randrange(0, len(self.cards), 3)

                # swap the randomly picked cards
                tmpCard = self.cards[x]
                self.cards[x] = self.cards[swap]
                self.cards[swap] = tmpCard

    def showHand(self):
        print('Hand')
        for c in self.cards:
            c.dump()
