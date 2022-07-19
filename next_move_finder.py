import time

from game import *


def board_input():
    '''gets the board from input'''
    final = []
    for i in range(8):
        row = []
        row_input = input()
        for j in range(8):
            row.append(row_input[j])
        final.append(row)
    return final

def board_output(board):
    output = ""
    for i in range(8):
        row = ""
        for j in range(8):
            output += board[i][j]
        if i != 7:
            output += "\n"
    return output

def imaginary_move(game, initial_xy, dest_xy):
    '''returns a whole new game in which move (init -> dest) has been played.
        does not affect the original game.'''
    new_game = Game()
    new_game.board = game.copy_board()
    new_game.turn = game.copy_turn()
    new_game.last_move = game.copy_last_move()
    new_game.took_a_piece_on_the_last_move = new_game.copy_took()
    new_game.move(initial_xy, dest_xy)

    return new_game

def minimax(game, alpha, beta, depth = 0):
    '''searches for best possible outcome.
        goes (DEPTH) level deep.
        '''

    if depth == DEPTH:
        """will not search further.
            returns current evaluation of the game"""
        return game.evaluation(), None

    turn = game.turn
    possible_moves = game.possible_moves()

    if turn == 'white':
        if len(possible_moves) == 0:
            """game is over
                black wins."""
            return -100000, None

        maxeval = -100000 #lower bound
        best_move = possible_moves[0]
        for move in possible_moves:
            imaginary_game = imaginary_move(game, move[0], move[1])
            eval, mv = minimax(imaginary_game, alpha, beta, depth+1)
            if eval >= maxeval:
                maxeval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                '''further searches will not find a better possible solution'''
                break
        return maxeval, best_move

    elif turn == 'black':
        if len(possible_moves) == 0:
            """game is over.
                white wins."""
            return 100000, None

        mineval = 100000
        best_move = possible_moves[0]
        for move in possible_moves:
            imaginary_game = imaginary_move(game, move[0], move[1])
            eval, mv = minimax(imaginary_game,alpha, beta, depth+1)
            if eval <= mineval:
                mineval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                '''further searches will not end to a better possible solution'''
                break
        return mineval, best_move


''''''''''''''''''''''''''''"""M A I N  P A R T"""'''''''''''''''''''''''''''

DEPTH = 12 #search depth
ALPHA = -100000 # -infinity
BETA = 100000 # +infinity
BOARD = []

def main():
    BOARD = board_input()   #receives the current board from input
    game = Game()
    game.board = BOARD
    game.turn = 'black' #since we're trying to find the best next move for black
    game.took_a_piece_on_the_last_move = False

    chain_of_moves = ""
    move_counts = 0
    evaluation = 0
    t = time.time()
    while(game.turn == 'black'):
        '''black could take a piece hence it gets to have another possible move to play'''
        eval, best_move = minimax(game, ALPHA, BETA)
        chain_of_moves += f"{best_move[0]} --> {best_move[1]} | "
        game.move(best_move[0], best_move[1])
        move_counts += 1
        evaluation = eval

        '''checks to see if white has any possibel moves'''
        if game.turn == 'white':
            if len(game.possible_moves()) == 0:
                '''game is over'''
                break
        else:
            game.turn = 'white'
            if len(game.possible_moves()) == 0:
                '''game is over'''
                break
            else:
                game.turn = 'black'


    print_all_stats = True
    if print_all_stats:
        print(f"runtime: {time.time() - t}")
        print(f"played move(s) : {chain_of_moves}")
        print(f"evaluation for this outcome with depth {DEPTH + move_counts - 1} is {evaluation}")
        print("final board after black's move is:")
    print(board_output(game.board))

    input("enter anything to exit")

if __name__ == '__main__':
    main()
