# Importing the necessary modules
import sys
from time import gmtime, strftime
# Defining an array to store the choice element number,initially it wil be null
class TicTacToeGame:
    def __init__(self):
        self.ChoiceArray = []


# The code to print the board
    def tictactoeboard(self):
        print(' ')
        print(' ' + self.ChoiceArray[0] + ' | ' + self.ChoiceArray[1] + ' | ' + self.ChoiceArray[
            2] + '    ' + '      ' + '1' + ' | ' + '2' + ' | ' + '3')
        print('-----------' + '        ' + '-----------')
        print(' ' + self.ChoiceArray[3] + ' | ' + self.ChoiceArray[4] + ' | ' + self.ChoiceArray[
            5] + '    ' + '      ' + '4' + ' | ' + '5' + ' | ' + '6')
        print('-----------' + '        ' + '-----------')
        print(' ' + self.ChoiceArray[6] + ' | ' + self.ChoiceArray[7] + ' | ' + self.ChoiceArray[
            8] + '    ' + '      ' + '7' + ' | ' + '8' + ' | ' + '9')
        print(' ')

    def game(self):
        number = 0
        turn = []
        winner = False
        dict = {1 : None}

        # Filling up the board with list comprehension
        self.ChoiceArray = [str(i + 1) for i in range(0, 9)]
        print("Please enter 0 if you are PLAYER 1 or 1 if you are PLAYER 2:")
        print("Who wants to start the game?")
        choice = int(input(">> "))
        # The player is either 0 or 1, no other input will be taken

        if choice == 0 or choice == 1:
            print("The entered player is valid")

        else:
            print("you have entered the wrong choice for the player")
            sys.exit()
        # The list 'turn' stores the chances of the players depending on who started the game first
        for j in range(0, 9):
            if j % 2 == 0:
                turn.append(bool(choice))

            else:
                turn.append(not bool(choice))
        print(turn)

        while not winner:
            self.tictactoeboard()

            # This will check if the moves are exhausted
            if number == 8:
                print("You have reached the end of this game")
                print("This game is a draw!!")
                sys.exit()

            # Implemented try/except
            try:
                choice = int(input(">> "))

            except:
                print("please enter valid number")
                continue
            # the choice cannot be greater than 9
            if choice > 9:
                print("The number cannot be greater than 9!")
                sys.exit()
            # checks for any moves that are being repeated
            if self.ChoiceArray[choice - 1] == 'X' or self.ChoiceArray[choice - 1] == 'O':
                print("illegal move")
                continue

            # if/elif block
            if turn[number] is False:
                self.ChoiceArray[choice - 1] = 'X'
            elif turn[number] is True:
                self.ChoiceArray[choice - 1] = 'O'

            # incrementing the counter
            number = number + 1

            # check for the winner
            for x in range(0, 3):
                y = x * 3
                if self.ChoiceArray[y] == self.ChoiceArray[(y + 1)] and self.ChoiceArray[y] == self.ChoiceArray[(y + 2)]:

                    winner = True
                    self.tictactoeboard()

                    if self.ChoiceArray[y] == 'X':
                        print("Player 1 is the winner")
                    else:
                        print("Player 2 is the winner")
                    sys.exit()

                if self.ChoiceArray[x] == self.ChoiceArray[(x + 3)] and self.ChoiceArray[x] == self.ChoiceArray[(x + 6)]:

                    winner = True
                    self.tictactoeboard()

                    if self.ChoiceArray[x] == 'X':
                        print("Player 1 is the winner")
                    else:
                        print("Player 2 is the winner")
                    sys.exit()

                if self.ChoiceArray[0] == self.ChoiceArray[4] and self.ChoiceArray[0] == self.ChoiceArray[8]:

                    winner = True
                    self.tictactoeboard()

                    if self.ChoiceArray[0] == 'X':

                        print("Player 1 is the winner")
                    else:
                        print("Player 2 is the winner")
                    sys.exit()
                elif self.ChoiceArray[2] == self.ChoiceArray[4] and self.ChoiceArray[4] == self.ChoiceArray[6]:
                    winner = True
                    self.tictactoeboard()
                    if self.ChoiceArray[2] == 'X':
                        # creating dictionary from dictionary comprehension
                        new_dict = {k: v for k, v in dict.items()}
                        new_dict.update({1: str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))})
                        print(new_dict)
                        print("Player 1 is the winner and he/she won at"+" "+new_dict[list(dict)[0]])

                    else:

                        new_dict = {k: v for k, v in dict.items()}
                        new_dict.update({1: str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))})
                        print(new_dict)
                        print("Player 2 is the winner and he/she won at"+" "+new_dict[list(dict)[0]])

                    sys.exit()


# implemented main,class and function
if __name__ == '__main__':
    ticTacToeGame = TicTacToeGame()
    ticTacToeGame.game()
