# Problem 3
# Write a Python program which implements a Tic-Tac-Toe game using the partial code provided in the Tutorial session. 
# The game must be between the computer and a real player. You can choose to use either minimax or Alpha-Beta algorithm.
# There's two versions, the first one is using a bit of the partial code.

# you are player x! computer is player o2

class TicTacToe():
    def __init__(self, state=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.state = state
        self.current_player = 1  #'x'= 1, 'o'= -1

    def make_move(self, row, col):
        if self.state[row][col] == 0:
            self.state[row][col] = self.current_player
            self.current_player *= -1  #Switch to the next player
            return True
        return False

    def is_winner(self, player):
        for i in range(3):
            if all(self.state[i][j] == player for j in range(3)) or \
               all(self.state[j][i] == player for j in range(3)):
                return True
        if all(self.state[i][i] == player for i in range(3)) or \
           all(self.state[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != 0 for row in self.state for cell in row)

    def is_game_over(self):
        return self.is_winner(1) or self.is_winner(-1) or self.is_draw()

    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    moves.append((i, j))
        return moves

    def print_board(self):
        for row in self.state:
            print(" ".join(['X' if cell == 1 else 'O' if cell == -1 else '.' for cell in row]))

    def play_game(self, human_player=True):
        while not self.is_game_over():
            self.print_board()
            print(f"Player {'X' if self.current_player == 1 else 'O'}'s turn:")
            if self.current_player == 1 or (self.current_player == -1 and not human_player):
                while True:
                    try:
                        row = int(input("Enter the row (0, 1, or 2): "))
                        col = int(input("Enter the column (0, 1, or 2): "))
                        if (row, col) in self.available_moves() and self.make_move(row, col):
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                #Computer's turn using Alpha-Beta
                row, col = self.alpha_beta_search()
                self.make_move(row, col)
                print(f"Computer's move: Row {row}, Column {col}")
        self.print_board()
        if self.is_winner(1):
            print("Player X wins!" if human_player else "Computer wins!")
        elif self.is_winner(-1):
            print("Player O wins!" if human_player else "Computer wins!")
        else:
            print("It's a draw!")

    def alpha_beta_search(self):
        _, best_move = self.max_value(-float('inf'), float('inf'))
        return best_move

    def max_value(self, alpha, beta):
        if self.is_game_over():
            return self.utility(), None

        v = -float('inf')
        best_move = None

        for move in self.available_moves():
            self.make_move(move[0], move[1])
            min_val, _ = self.min_value(alpha, beta)
            self.state[move[0]][move[1]] = 0

            if min_val > v:
                v = min_val
                best_move = move

            if v >= beta:
                return v, best_move

            alpha = max(alpha, v)

        return v, best_move

    def min_value(self, alpha, beta):
        if self.is_game_over():
            return self.utility(), None

        v = float('inf')
        best_move = None

        for move in self.available_moves():
            self.make_move(move[0], move[1])
            max_val, _ = self.max_value(alpha, beta)
            self.state[move[0]][move[1]] = 0

            if max_val < v:
                v = max_val
                best_move = move

            if v <= alpha:
                return v, best_move

            beta = min(beta, v)

        return v, best_move

    def utility(self):
        if self.is_winner(1):
            return 1
        elif self.is_winner(-1):
            return -1
        return 0


if "__main__":
    human_player = True  # Set to False to let the computer play against itself
    game = TicTacToe()
    game.play_game(human_player)








import math

#Initialize the Tic-Tac-Toe board states

class TicTacToe():
    def __init__(self, state=[[0,0,0],[0,0,0],[0,0,0]]):
        self.state = state

game = TicTacToe()
current_state = game.state

def init_board():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

#Draw the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(["X" if cell == 1 else "O" if cell == -1 else " " for cell in row]))
        if row != board[-1]:
            print("---------")

#To see if the board is full
def is_board_full(board):
    return all(cell != 0 for row in board for cell in row)

#Checking if one of the players has won the game
def check_winner(board, player):
    for combination in winning_combinations:
        if all(board[i // 3][i % 3] == player for i in combination):
            return True
    return False


def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = move // 3, move % 3
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == 0:
                return row, col
            else:
                print("You can't make that move, enter a number from 1-9.\nMake sure that the move is not taken already")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

#Computer's move implementing the alpha-beta algorithm
def computer_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        row, col = i // 3, i % 3
        if board[row][col] == 0:
            board[row][col] = 1
            score = alpha_beta(board, -math.inf, math.inf, False)
            board[row][col] = 0
            if score > best_score:
                best_score = score
                best_move = (row, col)

    return best_move

# Alpha-beta pruning algorithm
def alpha_beta(board, alpha, beta, is_maximizing):
    if check_winner(board, 1):
        return 1
    elif check_winner(board, -1):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_score = -float("inf")
        for i in range(9): #goes through the rows and columns
            row, col = i // 3, i % 3
            if board[row][col] == 0:
                board[row][col] = 1
                score = alpha_beta(board, alpha, beta, False)
                board[row][col] = 0
                max_score = max(score, max_score)
                alpha = max(alpha, max_score)
                if beta <= alpha:
                    break
        return max_score
    else:
        min_score = float("inf")
        for i in range(9):
            row, col = i // 3, i % 3
            if board[row][col] == 0:
                board[row][col] = -1
                score = alpha_beta(board, alpha, beta, True)
                board[row][col] = 0
                min_score = min(score, min_score)
                beta = min(beta, min_score)
                if beta <= alpha:
                    break
        return min_score


#Main game loop
def play_game():
    while True:
        board = init_board()
        display_board(board)

        while True:
            #Player's turn
            row, col = player_move(board)
            board[row][col] = -1
            display_board(board)

            if check_winner(board, -1):
                print("You win!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            #Computer's turn
            row, col = computer_move(board)
            board[row][col] = 1
            display_board(board)
            
            if check_winner(board, 1):
                print("Computer wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing. See you next time! - Tiffany.W")
            break

#call out the function to start
#play_game() <== uncomment this and comment the first version to run the second one!
