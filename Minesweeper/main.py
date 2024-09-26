import random

def create_board(rows, cols, bombs):
    board = [[0 for x in range(cols)] for y in range(rows)]
    bomb_count = 0
    while bomb_count < bombs:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != -1:
            board[row][col] = -1
            bomb_count += 1
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != -1:
                count = 0
                if row > 0 and col > 0 and board[row - 1][col - 1] == -1:
                    count += 1
                if row > 0 and board[row - 1][col] == -1:
                    count += 1
                if row > 0 and col < cols - 1 and board[row - 1][col + 1] == -1:
                    count += 1
                if col > 0 and board[row][col - 1] == -1:
                    count += 1
                if col < cols - 1 and board[row][col + 1] == -1:
                    count += 1
                if row < rows - 1 and col > 0 and board[row + 1][col - 1] == -1:
                    count += 1
                if row < rows - 1 and board[row + 1][col] == -1:
                    count += 1
                if row < rows - 1 and col < cols - 1 and board[row + 1][col + 1] == -1:
                    count += 1
                board[row][col] = count
    return board

def print_board(board, show_bombs=False):
    for row in board:
        for cell in row:
            if cell == -1 and not show_bombs:
                print("#", end=" ")
            elif isinstance(cell, int):
                print("#", end=" ")
            else:
                print(cell, end=" ")
        print()

def get_input():
    row = int(input("Enter row (1-5): ")) - 1
    col = int(input("Enter column (1-5): ")) - 1
    return row, col

def play_game():
    rows = 5
    cols = 5
    bombs = 5
    board = create_board(rows, cols, bombs)
    game_over = False
    while not game_over:
        row, col = get_input()
        if board[row][col] == -1:
            print("GAME OVER!")
            game_over = True
        else:
            board[row][col] = "1"
            print_board(board)

play_game()
