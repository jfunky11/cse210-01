def main():
  winner()
  pass
  
#has all combinations to win in order to get a winner
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or          
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[1] == board[4] == board[7] or
            board[2] == board[4] == board[6])
            
            
if __name__ == "__main__":
    main()
