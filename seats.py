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

def available_seats():
    number_of_available=0
    for i in board:
        for j in i:
            if j == "." :
                number_of_available += 1
    return number_of_available




def choose_seat():
    seat_row = (int(input("Input row:")) - 1)
    seat_col = (int(input("Input col:")) - 1)
    if (seat_row < 0 or seat_row > rows) or (seat_col < 0 or seat_col > rows):
        print("There is no such seat")
        return available_seats()
    elif (board[seat_row][seat_col] == "X"):
        print("This seat is already taken")
        return available_seats()
    else:
        board[seat_row][seat_col] = "X"
        return True

choose_seat()
print(available_seats())

print_board(board)
