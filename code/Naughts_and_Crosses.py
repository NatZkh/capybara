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

       