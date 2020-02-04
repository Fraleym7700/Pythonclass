import MichaelFraley_game_function as rps
import random

# Global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

# main function
def main():

    result = TIE

    while result==TIE:
        # Get computer number
        computer = random.randint(1, 3)

        # Get player number
        player = int(input('Enter 1 for rock, ' \
                           '2 for paper, 3 for scissors: '))

        print ('Computer chose', rps.choiceString(computer))
        print ('You chose', rps.choiceString(player))
        
        result = rps.rockPaperScissors(computer, player)
        
        if result == rps.TIE:
            print('You made the same choice as ' \
                  'the computer. Starting over')

    if (result == rps.COMPUTER_WINS):
        print ('The computer wins the game')
    elif result == rps.PLAYER_WINS:
        print ('You win the game')
    else:
        print ('You made an invalid choice. No winner')

# Call the main function.
if __name__ == "__main__":
    main()



