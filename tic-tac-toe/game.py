#Tic Tac Toe

board = [0, 1, 2],[3, 4, 5],[6, 7, 8]

def print_board(board):
    for i in range(3):
            print(str(board[i][0]) + ' | ' + str(board[i][1]) + ' | ' + str(board[i][2]))
            if i < 2:
                print('--+---+--')

def choose_simbol():
    print("Choose between O and X: ")
    player_symbol = input().strip().upper()  # Handle user input case insensitively and trim spaces
    while player_symbol not in ["O", "X"]:
        print("Symbol not available, try again.")
        player_symbol = input().strip().upper()
    
    player_1 = player_symbol
    
    if(player_1 == "O"):
        player_2 = "X"
    else:
        player_2 = "O"
    
    while(win()):
        play_game(player_1, board)
        play_game(player_2, board)    
    
def is_cell_available(board, x, y):
    if board[x][y] in ["X", "O"]:
        return False
    else:
        return True
    
def win():
    print("Win function")

def play_game(current_player, board):
    player_turn = True
    while(player_turn):
        print("Enter you move (e.g. 0,1 -> 4). The board starts with 0 and ends with 2.")
        player_move = input()
        
        x = int(player_move[0])
        y = int(player_move[2])
        
        x_available = x >= 0 and x <= 2
        y_available = y >= 0 and y <= 2
        
        if(x_available and y_available and is_cell_available(board, x, y)):
            #print(str(x) + ' ' + str(y))
            player_turn = False
            board[x][y] = current_player
            print_board(board)
            win()
        else:
            print("Position not available, try again.")
    
        
        

print_board(board)
choose_simbol()