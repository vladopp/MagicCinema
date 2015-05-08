import sqlite3
board = []
rows = 10

for x in range(rows):
    board.append(["."] * rows)

conn = sqlite3.connect("Reservations.db")
cursor = conn.cursor()

def print_board(board):
    for row in board:
        print(" ".join(row))

def can_choose_seat():
    seat_row = (int(input("Input row:")) - 1)
    seat_col = (int(input("Input col:")) - 1)
    if (seat_row < 0 or seat_row > rows) or (seat_col < 0 or seat_col > rows):
        print("There is no such seat")
        return can_choose_seat()
    elif (board[seat_row][seat_col] == "X"):
        print("This seat is already taken")
        return can_choose_seat()
    else:
        board[seat_row][seat_col] = "X"
        return True

can_choose_seat()

print_board(board)
