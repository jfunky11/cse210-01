def main():
  draw(board)
  pass

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
if __name__ == "__main__":
  main()
