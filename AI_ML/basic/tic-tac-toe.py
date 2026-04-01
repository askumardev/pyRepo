import random
import os

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'
        self.winner = None
        self.game_over = False

    def print_board(self):
        """Display the current state of the board"""
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        print("\nTIC TAC TOE")
        print("-----------")
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("-----------")
        print()

    def make_move(self, position):
        """Make a move on the board"""
        if self.board[position] == ' ' and not self.game_over:
            self.board[position] = self.current_player
            self.check_winner()
            self.switch_player()
            return True
        return False

    def switch_player(self):
        """Switch to the other player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        """Check if there's a winner or if it's a tie"""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                self.winner = self.board[i]
                self.game_over = True
                return

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                self.winner = self.board[i]
                self.game_over = True
                return

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.winner = self.board[0]
            self.game_over = True
            return
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.winner = self.board[2]
            self.game_over = True
            return

        # Check for tie
        if ' ' not in self.board:
            self.game_over = True

    def get_available_moves(self):
        """Return list of available moves"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def get_player_move(self):
        """Get valid move from human player"""
        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
                if 0 <= position <= 8 and self.board[position] == ' ':
                    return position
                else:
                    print("Invalid move! Choose an empty position (1-9).")
            except ValueError:
                print("Please enter a valid number (1-9).")

    def get_computer_move(self):
        """Get computer move (simple AI)"""
        available_moves = self.get_available_moves()
        
        # Try to win
        for move in available_moves:
            temp_board = self.board.copy()
            temp_board[move] = 'O'
            if self.check_winning_move(temp_board, 'O'):
                return move
        
        # Block opponent
        for move in available_moves:
            temp_board = self.board.copy()
            temp_board[move] = 'X'
            if self.check_winning_move(temp_board, 'X'):
                return move
        
        # Choose center if available
        if 4 in available_moves:
            return 4
        
        # Choose corners
        corners = [0, 2, 6, 8]
        available_corners = [corner for corner in corners if corner in available_moves]
        if available_corners:
            return random.choice(available_corners)
        
        # Choose any available move
        return random.choice(available_moves)

    def check_winning_move(self, board, player):
        """Check if a move would result in a win"""
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True

        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True

        # Check diagonals
        if board[0] == board[4] == board[8] == player:
            return True
        if board[2] == board[4] == board[6] == player:
            return True

        return False

def print_instructions():
    """Print game instructions"""
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered as follows:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\nEnter the number of the position where you want to place your mark.")
    input("Press Enter to continue...")

def main():
    print_instructions()
    
    while True:
        game = TicTacToe()
        
        # Choose game mode
        mode = input("\nChoose mode:\n1. Player vs Player\n2. Player vs Computer\nEnter choice (1 or 2): ")
        
        while mode not in ['1', '2']:
            mode = input("Invalid choice! Enter 1 or 2: ")
        
        vs_computer = (mode == '2')
        
        game.print_board()
        
        while not game.game_over:
            if game.current_player == 'X' or not vs_computer:
                position = game.get_player_move()
            else:
                print("Computer is thinking...")
                position = game.get_computer_move()
            
            if game.make_move(position):
                game.print_board()
        
        # Game over - display result
        if game.winner:
            if vs_computer and game.winner == 'O':
                print("Computer wins! Better luck next time!")
            else:
                print(f"Player {game.winner} wins!")
        else:
            print("It's a tie!")
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


# python3  AI_ML/basictic-tac-toe.py