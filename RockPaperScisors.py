import random
#Tahj McClain
#2/19/2024
#Comp 163/ Section 2
#Description- This program will use a seed to generate predicatable results for a Ro-Sham-Bo
#             game and then use while loops and a for loop to get the results of a game with the user input amount of rounds

# variables for game
rock = 0
paper = 1
scissors = 2

# seed to get the predictable results
seed = int(input('Seed : '))
random.seed(seed)
player1 = input("Player 1 Name : ")
player2 = input("Player 2 Name : ")
rounds = int(input("Rounds played : "))

# makes sure rounds > 0
while rounds <= 0: #
    print('Rounds must be > 0')
    rounds = int(input("Rounds played : "))

print(f'{player1} vs {player2} for {rounds} rounds')

# outputs the results from the random generated number using for and while loop incrementing current round only when a player wins
player1_win = 0
player2_win = 0
current_round = 0
for i in range(rounds):
    while current_round != rounds:
        player1_play = random.randint(0, 2)
        player2_play = random.randint(0, 2)
        
        if player1_play == player2_play:
            print('Tie')  
        elif (player1_play == rock and player2_play == scissors):
            print(f'{player1} wins with rock')
            player1_win += 1
            current_round += 1
        elif (player1_play == paper and player2_play == rock):
            print(f'{player1} wins with paper')
            player1_win += 1
            current_round += 1
        elif (player1_play == scissors and player2_play == paper):
            print(f'{player1} wins with scissors')
            player1_win += 1
            current_round += 1
        elif (player2_play == rock and player1_play == scissors):
            print(f'{player2} wins with rock')
            player2_win += 1
            current_round += 1
        elif (player2_play == paper and player1_play == rock):
            print(f'{player2} wins with paper')
            player2_win += 1
            current_round += 1
        elif (player2_play == scissors and player1_play == paper):
            print(f'{player2} wins with scissors')
            player2_win += 1
            current_round += 1
        
# displays results
print(f'{player1} wins {player1_win} and {player2} wins {player2_win}')
        