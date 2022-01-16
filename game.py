#plays game
def main():
    player = nextPlayer("")
    board = createBoard()
    while not (winner(board) or draw(board)):
        displayBoard(board)
        makeMove(player, board)
        player = nextPlayer(player)
    displayBoard(board)
    print("Good game. Thanks for playing!") 

#gives range of squares and creates the board
def createBoard():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

#displays how the board will look
def displayBoard(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

#makes the game end in a draw if all squares are used
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

#all combinations to win
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or          
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[1] == board[4] == board[7] or
            board[2] == board[4] == board[6])

#start next player's move
def makeMove(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

#determines whether the current player places an x or an o
def nextPlayer(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()
