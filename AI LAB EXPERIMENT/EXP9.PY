#function to display the board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)


#function to check the winner
def check_winner(board, player):
    #check rows
    for rows in board:
        if rows[0]==rows[1]==rows[2]==player:
          return True

    #check columns
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]!=" ":
          return True

    #check diagonals
    if board[0][0]==board[1][1]==board[2][2] != " ":
       return True

    if board[0][2]==board[1][1]==board[2][0] != " ":
       return True

    return False

#main program
board=[[" " for _ in range(3)] for _ in range(3)]
player="X"

for turn in range(9):
    print("\ncurrent board: ")
    print_board(board)

    print(f"player {player}'s turn")

    row=int(input("enter row (0,1,2): "))
    col=int(input("enter column (0,1,2): "))

    if board[row][col]==" ":
        board[row][col]=player

#check if current player has own
        if check_winner(board,player):
            print("\nfinal board:")
            print_board(board)
            print(f"player {player} wins!")
            break

#change player
        player="O" if player=="X" else "X"
    else:
      print("cell already occupied")

else:
    print("\nfinal board:")
    print_board(board)
    print("it's a draw")