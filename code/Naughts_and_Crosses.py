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

