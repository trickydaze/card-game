
import random
from collections import deque



class Card: #Card class to define cards in the deck
        def __init__(self, suit, val):
            self.suit = suit
            self.value = val

        def __repr__(self): #How the cards show on the output
            return '<{} of {}>'.format(self.value, self.suit)

deck_card=['Ace','Jack','King','Queen',1,2,3,4,5,6,7,8,9,10]

#Deck class to shuffle and draw the cards right
class Deck:

    def __init__(self):
        self.cards = deque()
        self.build()
    #in order to shuffle the cards
    def build(self):
        for i in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for j in deck_card:
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def length(self):
        return len(self.cards)
    #to eliminate getting the same cards
    def get_card(self):
        return self.cards.popleft()

played_cards=[]

#Player class to build the players
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def give_card(self, card):
        self.cards.append(card)

    def __repr__(self):  #to show each player and their cards before the start
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))

    def throw(self): #to throw the cards one by one
        if len(self.cards) > 0:
            played=self.cards.pop()
            played_cards.append(played) #Played Cards
            print(self.name,'drops',played)
            if len(self.cards) > 0:
                print(self.name, 'has', self.cards, 'remaining') #Active cards



#Game class to help build the game
class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def deal(self): #to deal the cards
        for player in self.players:
            for i in range(10):
                player.give_card(self.draw_card())


    def draw_card(self): #drawing the cards
        return self.deck.get_card()













