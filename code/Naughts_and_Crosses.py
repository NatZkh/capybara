game_state = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_game_state(game_state):
    print (game_state[0][0] + "|" + game_state[0][1] + "|" + game_state[0][2] +"\n" 
       + "—+—+—\n" 
       + game_state[1][0] + "|" + game_state[1][1] + "|" + game_state[1][2] + "\n" 
       + "—+—+—\n" 
       + game_state[2][0] + "|" + game_state[2][1] + "|" + game_state[2][2])


def player1_input():
    row = int(input ("Player 1, please input row number: "))
    col = int(input ("Player 1, please inout column number: "))
    p1_input = ("x", row, col)
    return p1_input

def player2_input():
    row = int (input ("Player 2, please input row number: "))
    col = int (input ("Player 2, please inout column number: "))
    p2_input = ("o", row, col)
    return p2_input

def update_game_status(game_state, game_command):
    game_state[game_command[1]][game_command[2]] = game_command[0]
    return game_state

class GameState:
    def __init__ (self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        self.current_player = "x"
        
    def print_game_state(self):
        print (self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2] +"\n" 
            + "—+—+—\n" 
            + self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2] + "\n" 
            + "—+—+—\n" 
            + self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2])
        
    def apply_move(self, move):
        if self.board[move[0]][move[1]] == " ":
            self.board[move[0]][move[1]] = self.current_player
            if self.current_player == "x":
                self.current_player = "o"
            else:
                self.current_player = "x"
            return True
        else:
            return False 
    
    def get_game_status(self):
        if self.is_winner("x"):
            return "Congrats, player X wins!"
        elif self.is_winner("o"):
            return "Congrats, player O wins!"
        elif self.board_full():
            return "It's a draw!"
        else:
            return "ongoing"
    
    def is_winner(self, player):
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        elif self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        elif self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        elif self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        elif self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        elif self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        else:
            return False
    
    def board_full(self):
        for row in self.board: 
            for cell in row:
                if cell == " ":
                    return False
        return True

def get_player_move(game_state):
    row = int(input("Player " + game_state.current_player + ", please chose row number:"))
    col = int (input("Player " + game_state.current_player + ", please chose column number:"))
    move = (row,col)
    return move

#game code
game = GameState()
game.print_game_state()
move = get_player_move(game)
while game.apply_move(move) is False:
    print ("This cell is already taken. Try again")
    move = get_player_move(game)
game.print_game_state()
while game.get_game_status() == "ongoing":
    move = get_player_move(game)
    while game.apply_move(move) is False:
        print ("This cell is already taken. Try again")
        move = get_player_move(game)
    game.print_game_state()
print (game.get_game_status())

#to do = verify the input to be integer; loop to ask for new input in case it's not
#GameState class in the constructor should take the size of the board. Win condition should be relarive to board size