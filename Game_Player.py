#Dimitri Makrigiorgos

from Board_Class import Board
from Player_Class import Player
from AI_Player_Class import AIPlayer
import random

def process_move(player, board):
    '''takes a Player for the player whose move
    is being processed, and a Board for the game that is being played.
    Performs all the steps involved in processing a single move by player on
    board
    '''
    print(str(player) + "'s turn")
    nm = player.next_move(board)
    board.add_checker(player.checker,nm)
    print()
    print(board)
    if board.is_win_for(player.checker):
        print()
        print(str(player) + ' wins in ' + str(player.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    if board.is_full():
        print()
        print("It's a tie!")
        return True
    else:
        print()
        return False
        
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board  as it looks at the end of the game.
        player1 and player2 are objects representing Connect Four
        players.
        One of them should use 'X' checkers and the other should
        use 'O' checkers.
    """
    # Resets number of moves to 0, in case multiple games are played
    player1.num_moves = 0
    player2.num_moves = 0
    # Make sure that one is 'X' and one is 'O'
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('To play the game, you need one X player and one O player.')
        return None

    print('Thanks for playing my Connect Four game! Good luck, and may the odds be ever in your favor!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
            
            
        

    
    
    
