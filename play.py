from game import *
from next_move_finder import *


def print_indexed_board(board):
    output = "X01234567X\n"
    for i in range(8):
        row = f"{i}"
        for j in range(8):
            row += board[i][j]
        row += f"{i}\n"

        output += row
    output += "X01234567X"
    print(output)


CUSTOM_BOARD = False
PLAYER_1 = 'ai' #white
PLAYER_2 = 'ai' #black
'''player types:1. 'human' or 2. 'ai'  '''



def main():
    game = Game()
    if CUSTOM_BOARD:
        print("enter 8x8 board")
        game.board = board_input()
        turn = input("who plays first? [w/b]")
        if turn == 'b':
            game.turn = 'black'

    count = 0
    while not game.over and count < 100:
        print(count)
        count += 1
        print("current board")
        print_indexed_board(game.board)

        #white's turn
        if game.turn == 'white':
            if PLAYER_1 == 'human':
                print("white to go: [x1 y1 x2 y2]")
                x1, y1, x2, y2 = input().split()
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                game.move((x1, y1), (x2, y2))

            elif PLAYER_1 == 'ai':
                eval, move = minimax(game, ALPHA, BETA)
                game.move(move[0], move[1])
                print(f"ai move was {move[0]} --> {move[1]}")

            if len(game.possible_moves()) == 0 and game.turn == 'black':
                game.over = True
                print("WHITE WON")
                break
        print("current board")
        print_indexed_board(game.board)
        #black's turn
        if game.turn == 'black':
            if PLAYER_2 == 'human':
                print("black to go: [x1 y1 x2 y2]")
                x1, y1, x2, y2 = input().split()
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                game.move((x1, y1), (x2, y2))

            elif PLAYER_2 == 'ai':
                eval, move = minimax(game, ALPHA, BETA)
                game.move(move[0], move[1])
                print(f"ai move was {move[0]} --> {move[1]}")

            if len(game.possible_moves()) == 0 and game.turn == 'white':
                game.over = True
                print("BLACK WON")
                break


if __name__ == '__main__':
    main()