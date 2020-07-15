import json
import card

stats = dict(
    h1Face = 0,
    h2Face = 0,
    h1Favorite = False,
    h2Favorite = False,
    wars = 0,
    handsPlayed = 0,
    shuffles = 0,
)
atWar = True
done = False
played = 0

#Create the deck
d = card.Deck()
print('Deck created.')

#Shuffle the deck
d.shuffle()
print('Deck shuffled.')

# Create empty hands
h1 = card.Hand()
h2 = card.Hand()

# Create the pot
pot = []

h1Face = 0
h2Face = 0

# Initialize 'Deal' the hands
for cnt in range( 0, card.MAX_HAND_SIZE ):
    h1.cards.append( d.deal( 1 ) )
    h2.cards.append( d.deal( 1 ) )

# Analyze the Hands to see who is the favorite.
for cnt in range( 0, card.MAX_HAND_SIZE):
    if (h1.cards[cnt].value >= 9):
        h1Face += 1

    if (h2.cards[cnt].value >= 9):
        h2Face += 1

stats['h1Face'] = h1Face
stats['h2Face'] = h2Face

if h1Face > h2Face:
        stats['h1Favorite'] = True
        stats['h2Favorite'] = False
        print(f'H1 is the Favorite: [{h1Face}] vs [{h2Face}]')
elif h2Face > h1Face:
        stats['h1Favorite'] = False
        stats['h2Favorite'] = True
        print(f'H2 is the Favorite: [{h1Face}] vs [{h2Face}]')
else:
        stats['h1Favorite'] = False
        stats['h2Favorite'] = False
        print(f'Even Odds!: [{h1Face}] vs [{h2Face}]')

while done == False:
    stats['handsPlayed'] += 1

    # Shuffle the cards every time through the deck.
    if (stats['handsPlayed'] % 26 == 0):
        stats['shuffles'] += 1
        h1.shuffle()
        h2.shuffle()

    if (h1.cardsLeft() == 0 or h2.cardsLeft() == 0):
        done = True
        print('Game Over[{pcnt}, {shuff}]: h1({h1cnt}) to h2({h2cnt})'.format(
                pcnt = stats['handsPlayed'],
                shuff = stats['shuffles'],
                h1cnt = len(h1.cards), 
                h2cnt = len(h2.cards))
                )

        with open("war-game-results.json", "w") as jsonFile:
            json.dump(stats, jsonFile)
        break

#    print('Play({cnt}): h1[{card1}] vs h2[{card2}]'.format (cnt = played, card1 = h1.seeCard().value, card2 = h2.seeCard().value))

    # Determine who played the highest card 
    if (h1.seeCard().value > h2.seeCard().value):

       # Reconcile the pot
       pot.append(h1.playCard())
       pot.append(h2.playCard())

       h1.cards.extend(pot)

       pot = []

    elif (h1.seeCard().value < h2.seeCard().value):
        # Reconcile the pot
        pot.append(h1.playCard())
        pot.append(h2.playCard())

        h2.cards.extend(pot)

        pot = []
    else:
        print('We started a new war')
        stats['wars'] += 1

        # Update the current pot before repeating loop
        pot.append(h1.playCard())
        pot.append(h2.playCard())

        # Play an extra card (another will happen when loop restarts)
        # according to the rules of War.
        #
        # If a player is out of cards - end the game after pulling in the pot.
        if (h1.cardsLeft() == 0):
            done = True
            h2.cards.extend(pot)
        elif (h2.cardsLeft() == 0):
            done = True;
            h1.cards.extend(pot)
        else:
            pot.append(h1.playCard())
            pot.append(h2.playCard())