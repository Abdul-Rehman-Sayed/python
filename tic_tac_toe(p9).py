def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    return (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player)

def is_board_full(board):
    return ' ' not in board

def play_game():
    board = [' ' for _ in range(9)]
    position_map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    print("Welcome to Tic Tac Toe!\n")
    print("Position Guide:")
    print_board(position_map)

    current_player = 'X'

    while True:
        print_board(board)
        while True:
            try:
                position = int(input(f"Player {current_player}, enter position (1-9): ").strip()) - 1
                if 0 <= position <= 8 and board[position] == ' ':
                    board[position] = current_player
                    break
                else:
                    print("Invalid position. The position is either already taken or out of range.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
