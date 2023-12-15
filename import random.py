import random

class TicTacToe:

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.turn = 'X'

    def is_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
                return True
            if self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
                return True
        return False

    def get_available_moves(self):
        available_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    available_moves.append((i, j))
        return available_moves

    def make_move(self, move):
        self.board[move[0]][move[1]] = self.turn
        self.turn = 'O' if self.turn == 'X' else 'X'

    def minimax(self, depth, maximizing_player):
        if depth == 3:
            if self.is_winner('X'):
                return 1
            elif self.is_winner('O'):
                return -1
            else:
                return 0

        available_moves = self.get_available_moves()
        if not available_moves:
            return 0

        if maximizing_player:
            best_score = -float('inf')
            for move in available_moves:
                new_board = self.copy_board()
                new_board.make_move(move)
                score = new_board.minimax(depth + 1, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in available_moves:
                new_board = self.copy_board()
                new_board.make_move(move)
                score = new_board.minimax(depth + 1, True)
                best_score = min(best_score, score)
            return best_score

    def copy_board(self):
        new_board = TicTacToe()
        new_board.board = [row[:] for row in self.board]
        new_board.turn = self.turn
        return new_board


def main():
    game = TicTacToe()
    while not game.is_winner('X') and not game.is_winner('O'):
        if game.turn == 'X':
            move = input('Joueur X, entrez votre coup (x, y): ')
            move = tuple(map(int, move.split(',')))
        else:
            move = game.minimax(0, True)
        game.make_move(move)
        game.print_board()

    if game.is_winner('X'):
        print('Joueur X a gagné !')
    elif game.is_winner('O'):
        print('Joueur O a gagné !')
    else:
        print('Match nul !')


if __name__ == '__main__':
    main()
