# Connect_Four
A connect four game. You can play with two human players, play against a semi-intelligent AI, or watch two AIs play each other!

AIPlayer:
  The AIPlayer "looks ahead" a certain number of moves based on a recursive function, depending on what number you enter as your       lookahead (see below for instructions). It will rate each potential move with a score, and choose the maximum score for where to go. If some moves have an equivalent score, the AI will make a decision where to go based on the tiebreak that you chose when you defined the AIPlayer (see below). The options are either "LEFT", "RIGHT", or "RANDOM".


INSTRUCTIONS TO PLAY:

1. Download all four files into a directory.
2. Run the "Game_Player" module in a shell (I've been using IDLE - to do this in IDLE, edit the game_player.py file with idle, then go to "Run" at the top and click "Run Module")
3. Define who you want your players for the game to be: to define a Player, enter the name of the player, and then enter = Player("X") or Player("O"). This will create a new Player object with the Checker "X" or the Checker "O", based on which checker you chose. "X" and "O" are the only valid checkers in Connect 4. EXAMPLE: Player_1 = Player("X") 
4. If you want to create an AIPlayer,you have a few options. First, you must enter the checker "X" or "O". Then, you must enter a "tiebreak" method. The options are either "LEFT", "RIGHT", or "RANDOM". Finally, you must enter the number of turns that you want the AIPlayer to look ahead. A higher lookahead number will generally create a smarter AIPlayer, because they are looking further ahead at all possiblities and choosing the best one. However, as it is a recursive formula that checks every possible move in every spot, the higher the number, the longer the AI will take to make its move. If you keep the lookahead below 5, the AI will usually respond instantaneously. EXAMPLE: Player_2 = AIPlayer("O", "LEFT", 3)
5. Once you have defined the players that you want to play the game with, its time to start! Type connect_four(Player_1, Player_2) (assuming that is how you named your players), and the game should begin. One of the players must be using checker "X" while the other uses checker "O". From there, it is pretty simple, the program should contain directions to play - the first to get four in a row in any direction wins!
6. Have fun!!!

