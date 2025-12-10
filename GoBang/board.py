LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

class Board:
    def __init__(self,length):
        self.length = length
        self.board = [None] * self.length
        for i in range(len(self.board)):
            if i+1 >=10:
                self.board[i] = [f"{i+1}"]+[f"{'⚪':1}"] * self.length
            else:
                self.board[i] = [f"{i+1} "] + [f"{'⚪':1}"] * self.length

    def print_board(self):
        print("   ",end=" ")
        # print all the letters
        for k in range (len(self.board)):
                print(f"{LETTERS[k]}  ", end="")
        print("")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ") #The end parameter is used to append any string at the end of the output of the print statement in python. By default, the print method ends with a newline.
            print("")

    def add_piece(self, icon):
        if self.isGameContinue():
            print(f"\n=== Player {icon} ===")
            column_input = ''
            while column_input not in LETTERS[:self.length]:
                column_input = input('Column Letter: ')
            column = LETTERS.index(column_input)+1
            row_input = 10000
            while row_input not in range(self.length):
                try:
                    row_input = int(input('Row Number: '))
                except ValueError:
                    continue
            row = row_input-1

            if self.board[row][column] == '⚪':
                self.board[row][column] = icon
                self.print_board()
            else:
                print("Please choose an empty position!")
                self.add_piece(icon)



    def isGameContinue(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] != '⚪':
                    if y <= self.length-4:
                        if self.board[x][y] == self.board[x][y+1] == self.board[x][y+2] == self.board[x][y+3] == self.board[x][y+4]:
                            self.win_game(x,y)
                            return False
                    if x <= self.length-5:
                        if self.board[x][y] == self.board[x+1][y] == self.board[x+2][y] == self.board[x+3][y] == self.board[x+4][y]:
                            self.win_game(x,y)
                            return False
                    # from top left to bottom right
                    if y <= self.length-4 and x <= self.length-5:
                        if self.board[x][y] == self.board[x+1][y+1] == self.board[x+2][y+2] == self.board[x+3][y+3] == self.board[x+4][y+4]:
                            self.win_game(x,y)
                            return False
                    #from bottom left to top right
                    if y<= self.length-4 and x >= 4:
                        if self.board[x][y] == self.board[x-1][y+1] == self.board[x-2][y+2] == self.board[x-3][y+3] == self.board[x-4][y+4]:
                            self.win_game(x, y)
                            return False
        return True

    def win_game(self,x,y):
        player = self.board[x][y]
        print (f'Player {player} Wins!')

