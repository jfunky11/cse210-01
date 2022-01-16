from createBoard import createBoard
from displayBoard import displayBoard
from draw import draw
from winner import winner
from makeMove import makeMove
from nextPlayer import nextPlayer

def main():
    player = nextPlayer("")
    board = createBoard()
    while not (winner(board) or draw(board)):
        displayBoard(board)
        makeMove(player, board)
        player = nextPlayer(player)
    displayBoard(board)
    print("Good game. Thanks for playing!") 

if __name__ == "__main__":
    main()
