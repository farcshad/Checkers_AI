START_BOARD = [
    ['E', 'b', 'E', 'b', 'E', 'b', 'E', 'b'],
    ['b', 'E', 'b', 'E', 'b', 'E', 'b', 'E'],
    ['E', 'b', 'E', 'b', 'E', 'b', 'E', 'b'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['w', 'E', 'w', 'E', 'w', 'E', 'w', 'E'],
    ['E', 'w', 'E', 'w', 'E', 'w', 'E', 'w'],
    ['w', 'E', 'w', 'E', 'w', 'E', 'w', 'E']
]

class Game:
    over = None
    board = None
    turn = None
    last_move = None
    took_a_piece_on_the_last_move = False



    def __init__(self):
        self.turn = 'white' #  'white' and 'black'
        self.board = START_BOARD
        self.over = False


    def copy_board(self):
        new_board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(self.board[i][j])
            new_board.append(row)
        return new_board

    def copy_turn(self):
        if self.turn == 'white':
            return 'white'
        else:
            return 'black'
    def copy_last_move(self):
        last_move = self.last_move
        if last_move == None:
            return None
        new_x = 0
        new_y = 0
        new_x += last_move[0]
        new_y += last_move[1]
        return (new_x, new_y)

    def copy_took(self):
        if self.took_a_piece_on_the_last_move:
            return True
        else:
            return False

    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(8):
            print(self.board[i])

    def move(self, inital_xy, dest_xy):

        x_1, y_1 = inital_xy
        x_2, y_2 = dest_xy
        x_dif = max(x_1 - x_2, x_2 - x_1)
        y_dif = max(y_1 - y_2, y_2 - y_1)
        if x_dif > 2 or y_dif > 2 or x_dif != y_dif:
            return 'invalid move'

        piece = self.board[x_1][y_1]
        self.board[x_1][y_1] = 'E'
        if piece == 'w' and x_2 == 0:
            piece = 'W'
        elif piece == 'b' and x_2 == 7:
            piece = 'B'
        self.board[x_2][y_2] = piece
        self.last_move = (x_2, y_2)
        if x_dif < 2:
            self.took_a_piece_on_the_last_move = False
            if self.turn == 'white':
                self.turn = 'black'
            else:
                self.turn = 'white'
        if x_dif == 2:
            self.took_a_piece_on_the_last_move = True
            self.board[int((x_1 + x_2) / 2)][int((y_1 + y_2) / 2)] = 'E'

    def possible_moves(self):
        capture_possible = False
        possible_moves = []
        if self.turn == 'white':
            if self.took_a_piece_on_the_last_move:
                x, y = self.last_move
                possible_moves.append(((x,y), (x,y)))
                if 0 <= x - 1 < 8 and 0 <= y - 1 < 8:
                    if self.board[x - 1][y - 1] == 'b' or self.board[x - 1][y - 1] == 'B':
                        if 0 <= x - 2 < 8 and 0 <= y - 2 < 8 and self.board[x - 2][y - 2] == 'E':
                            possible_moves.append(((x, y), (x - 2, y - 2)))

                if 0 <= x - 1 < 8 and 0 <= y + 1 < 8:
                    if self.board[x - 1][y + 1] == 'b' or self.board[x - 1][y + 1] == 'B':
                        if 0 <= x - 2 < 8 and 0 <= y + 2 < 8 and self.board[x - 2][y + 2] == 'E':
                            possible_moves.append(((x, y), (x - 2, y + 2)))

                if self.board[x][y] == 'W':
                    if 0 <= x + 1 < 8 and 0 <= y - 1 < 8:
                        if self.board[x + 1][y - 1] == 'b' or self.board[x + 1][y - 1] == 'B':
                            if 0 <= x + 2 < 8 and 0 <= y - 2 < 8 and self.board[x + 2][y - 2] == 'E':
                                possible_moves.append(((x, y), (x + 2, y - 2)))

                    if 0 <= x + 1 < 8 and 0 <= y + 1 < 8:
                        if self.board[x + 1][y + 1] == 'b' or self.board[x + 1][y + 1] == 'B':
                            if 0 <= x + 2 < 8 and 0 <= y + 2 < 8 and self.board[x + 2][y + 2] == 'E':
                                possible_moves.append(((x, y), (x + 2, y + 2)))
            else:
                for x in range(8):
                    for y in range(8):
                        if self.board[x][y] == 'W' or self.board[x][y] == 'w':
                            if 0 <= x - 1 < 8 and 0 <= y - 1 < 8:
                                if self.board[x - 1][y - 1] == 'b' or self.board[x - 1][y - 1] == 'B':
                                    if 0 <= x - 2 < 8 and 0 <= y - 2 < 8 and self.board[x - 2][y - 2] == 'E':
                                        if capture_possible:
                                            possible_moves.append(((x, y), (x - 2, y - 2)))
                                        else:
                                            capture_possible = True
                                            possible_moves = []
                                            possible_moves.append(((x, y), (x - 2, y - 2)))
                                elif self.board[x - 1][y - 1] == 'E':
                                    if not capture_possible:
                                        possible_moves.append(((x, y), (x - 1, y - 1)))

                            if 0 <= x - 1 < 8 and 0 <= y + 1 < 8:
                                if self.board[x - 1][y + 1] == 'b' or self.board[x - 1][y + 1] == 'B':
                                    if 0 <= x - 2 < 8 and 0 <= y + 2 < 8 and self.board[x - 2][y + 2] == 'E':
                                        if capture_possible:
                                            possible_moves.append(((x, y), (x - 2, y + 2)))
                                        else:
                                            capture_possible = True
                                            possible_moves = []
                                            possible_moves.append(((x, y), (x - 2, y + 2)))
                                elif self.board[x - 1][y + 1] == 'E':
                                    if not capture_possible:
                                        possible_moves.append(((x, y), (x - 1, y + 1)))

                            if self.board[x][y] == 'W':
                                if 0 <= x + 1 < 8 and 0 <= y - 1 < 8:
                                    if self.board[x + 1][y - 1] == 'b' or self.board[x + 1][y - 1] == 'B':
                                        if 0 <= x + 2 < 8 and 0 <= y - 2 < 8 and self.board[x + 2][y - 2] == 'E':
                                            if capture_possible:
                                                possible_moves.append(((x, y), (x + 2, y - 2)))
                                            else:
                                                capture_possible = True
                                                possible_moves = []
                                                possible_moves.append(((x, y), (x + 2, y - 2)))
                                    elif self.board[x + 1][y - 1] == 'E':
                                        if not capture_possible:
                                            possible_moves.append(((x, y), (x + 1, y - 1)))

                                if 0 <= x + 1 < 8 and 0 <= y + 1 < 8:
                                    if self.board[x + 1][y + 1] == 'b' or self.board[x + 1][y + 1] == 'B':
                                        if 0 <= x + 2 < 8 and 0 <= y + 2 < 8 and self.board[x + 2][y + 2] == 'E':
                                            if capture_possible:
                                                possible_moves.append(((x, y), (x + 2, y + 2)))
                                            else:
                                                capture_possible = True
                                                possible_moves = []
                                                possible_moves.append(((x, y), (x + 2, y + 2)))
                                    elif self.board[x + 1][y + 1] == 'E':
                                        if not capture_possible:
                                            possible_moves.append(((x, y), (x + 1, y + 1)))

        else:
            if self.took_a_piece_on_the_last_move:
                x, y = self.last_move
                possible_moves.append(((x,y), (x,y)))
                if 0 <= x + 1 < 8 and 0 <= y - 1 < 8:
                    if self.board[x + 1][y - 1] == 'w' or self.board[x + 1][y - 1] == 'W':
                        if 0 <= x + 2 < 8 and 0 <= y - 2 < 8 and self.board[x + 2][y - 2] == 'E':
                            possible_moves.append(((x, y), (x + 2, y - 2)))

                if 0 <= x + 1 < 8 and 0 <= y + 1 < 8:
                    if self.board[x + 1][y + 1] == 'w' or self.board[x + 1][y + 1] == 'W':
                        if 0 <= x + 2 < 8 and 0 <= y + 2 < 8 and self.board[x + 2][y + 2] == 'E':
                            possible_moves.append(((x, y), (x + 2, y + 2)))

                if self.board[x][y] == 'B':
                    if 0 <= x - 1 < 8 and 0 <= y - 1 < 8:
                        if self.board[x - 1][y - 1] == 'w' or self.board[x - 1][y - 1] == 'W':
                            if 0 <= x - 2 < 8 and 0 <= y - 2 < 8 and self.board[x - 2][y - 2] == 'E':
                                possible_moves.append(((x, y), (x - 2, y - 2)))

                    if 0 <= x - 1 < 8 and 0 <= y + 1 < 8:
                        if self.board[x - 1][y + 1] == 'w' or self.board[x - 1][y + 1] == 'W':
                            if 0 <= x - 2 < 8 and 0 <= y + 2 < 8 and self.board[x - 2][y + 2] == 'E':
                                possible_moves.append(((x, y), (x - 2, y + 2)))
            else:
                for x in range(8):
                    for y in range(8):
                        if self.board[x][y] == 'b' or self.board[x][y] == 'B':
                            if 0 <= x + 1 < 8 and 0 <= y - 1 < 8:
                                if self.board[x + 1][y - 1] == 'w' or self.board[x + 1][y - 1] == 'W':
                                    if 0 <= x + 2 < 8 and 0 <= y - 2 < 8 and self.board[x + 2][y - 2] == 'E':
                                        if capture_possible:
                                            possible_moves.append(((x, y), (x + 2, y - 2)))
                                        else:
                                            capture_possible = True
                                            possible_moves = []
                                            possible_moves.append(((x, y), (x + 2, y - 2)))
                                elif self.board[x + 1][y - 1] == 'E':
                                    if not capture_possible:
                                        possible_moves.append(((x, y), (x + 1, y - 1)))

                            if 0 <= x + 1 < 8 and 0 <= y + 1 < 8:
                                if self.board[x + 1][y + 1] == 'w' or self.board[x + 1][y + 1] == 'W':
                                    if 0 <= x + 2 < 8 and 0 <= y + 2 < 8 and self.board[x + 2][y + 2] == 'E':
                                        if capture_possible:
                                            possible_moves.append(((x, y), (x + 2, y + 2)))
                                        else:
                                            capture_possible = True
                                            possible_moves = []
                                            possible_moves.append(((x, y), (x + 2, y + 2)))
                                elif self.board[x + 1][y + 1] == 'E':
                                    if not capture_possible:
                                        possible_moves.append(((x, y), (x + 1, y + 1)))

                            if self.board[x][y] == 'B':
                                if 0 <= x - 1 < 8 and 0 <= y - 1 < 8:
                                    if self.board[x - 1][y - 1] == 'w' or self.board[x - 1][y - 1] == 'W':
                                        if 0 <= x - 2 < 8 and 0 <= y - 2 < 8 and self.board[x - 2][y - 2] == 'E':
                                            if capture_possible:
                                                possible_moves.append(((x, y), (x - 2, y - 2)))
                                            else:
                                                capture_possible = True
                                                possible_moves = []
                                                possible_moves.append(((x, y), (x - 2, y - 2)))
                                    elif self.board[x - 1][y - 1] == 'E':
                                        if not capture_possible:
                                            possible_moves.append(((x, y), (x - 1, y - 1)))

                                if 0 <= x - 1 < 8 and 0 <= y + 1 < 8:
                                    if self.board[x - 1][y + 1] == 'w' or self.board[x - 1][y + 1] == 'W':
                                        if 0 <= x - 2 < 8 and 0 <= y + 2 < 8 and self.board[x - 2][y + 2] == 'E':
                                            if capture_possible:
                                                possible_moves.append(((x, y), (x - 2, y + 2)))
                                            else:
                                                capture_possible = True
                                                possible_moves = []
                                                possible_moves.append(((x, y), (x - 2, y + 2)))
                                    elif self.board[x - 1][y + 1] == 'E':
                                        if not capture_possible:
                                            possible_moves.append(((x, y), (x - 1, y + 1)))
        return possible_moves

    def evaluation(self):
        normal_value = 3
        king_value = 5
        eval = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'w':
                    eval += normal_value

                elif self.board[i][j] == 'W':
                    eval += king_value

                elif self.board[i][j] == 'b':
                    eval -= normal_value

                elif self.board[i][j] == 'B':
                    eval -= king_value

        return eval

