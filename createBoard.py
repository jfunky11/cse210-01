def main():
  createBoard()
  pass

#gives range of squares and creates the board
def createBoard():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board
  
if __name__ == '__main__':
    main()
