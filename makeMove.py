def main():
  makeMove()
  pass
  
#start next player's move
def makeMove(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player
    
if __name__ == "__main__":
    main()
