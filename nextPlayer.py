def main():
  nextPlayer()  
  pass
  
def nextPlayer(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
        
if __name__ == "__main__":
    main()
