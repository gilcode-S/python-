import random as ran

options = ("rock", 'paper', 'scissors')

running = True

while running:
    player = None
    computer = ran.choice(options)

    while player not in options:
        player = input("Enter a choice: (rock, paper, scissors): ")

        print(f'Player: {player}')
        print(f'Computer: {computer}')

        # win condition

        if player == computer:
            print('Its a tie!')
        elif player == 'rock' and computer == 'scissors':
            print("You win")
        elif player == 'paper' and computer == 'rock':
            print("you win")
        elif player == 'scissors' and computer == 'paper':
            print('you win')
        else:
            print('you lose, computer win')
        if not input("play again (y/n) ? : ").lower() == "y":
            running = False


print("Thanks for playing")
