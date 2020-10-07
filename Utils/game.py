deck_of_cards = Deck()
player_one=Player(input("Player One: Please put your name:"))
player_two = Player(input("Player Two: Please put your name:"))
players=[player_one,player_two]
player_number=input('If you would like to add more players, please type "Y"')
print(player_number)
if player_number == "Y":
    player_three = Player(input("Player Three: Please put your name:"))
    players.append(player_three)
else:
    print("Let's begin...")

new_game = Game(players, deck_of_cards)
new_game.deal()
print(players)
#function to navigate the throw() function in class
def finish_cards():
    for n in players:
     n.throw()


#loop the finish_cards function
while players:
    finish_cards()
    if len(played_cards) >19:
        break
print('Game Over!')
print('Cards that have played are', played_cards)
print('In this game everyone is a winner!')