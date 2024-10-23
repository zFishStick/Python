#Tic Tac Toe

board = [0, 1, 2],[3, 4, 5],[6, 7, 8]

def print_board(board):
    for i in range(3):
            print(str(board[i][0]) + ' | ' + str(board[i][1]) + ' | ' + str(board[i][2]))
            if i < 2:
                print('--+---+--')

def choose_simbol():
    print("Welcome to Tic-Tac-Toe!")
    print("Please, choose between O and X: ")
    player_symbol = input().strip().upper()  # Handle user input case insensitively and trim spaces
    while player_symbol not in ["O", "X"]:
        print("Symbol not available, try again.")
        player_symbol = input().strip().upper()
                
    current_player = player_symbol
    
    play_game(current_player, board) 
    
def is_cell_available(board, x, y):
    if board[x][y] in ["X", "O"]:
        return False
    else:
        return True
    
def win(current_player, board):
    
    for row in board:
        if all([cell == current_player for cell in row]):
            print(current_player + " is the winner")
            return False

    # Controlla le colonne
    for col in range(3):
        if all([board[row][col] == current_player for row in range(3)]):
            print(current_player + " is the winner")
            return False

    # Controlla la diagonale principale
    if all([board[i][i] == current_player for i in range(3)]):
        print(current_player + " is the winner")
        return False

    # Controlla la diagonale secondaria
    if all([board[i][2 - i] == current_player for i in range(3)]):
        print(current_player + " is the winner")
        return False
    
    
    return True

def play_game(current_player, board):
    player_turn = True
    while(player_turn):
        print("Enter you move (e.g. 0,1 -> 4). The board starts with 0 and ends with 2.")
        player_move = input()
        
        player_move = player_move.split(',', 1) #['0','1']
        
        if(player_move[0].isnumeric and player_move[1].isnumeric):
            x = int(player_move[0])
            y = int(player_move[1])
            x_available = x >= 0 and x <= 2
            y_available = y >= 0 and y <= 2
                   
            if(x_available and y_available and is_cell_available(board, x, y)):
                player_turn = False
                board[x][y] = current_player
                print_board(board)
                end_game = win(current_player, board)
                if(end_game):
                    current_player = 'O' if current_player == 'X' else 'X'
                    play_game(current_player, board)
                else:
                    print("Fine del gioco")
                    player_turn = False
            else:
                print("Position not available, try again.")
    
        
        

print_board(board)
choose_simbol()