import sqlite3
import sys
import time


def helpp():
    print("""You can use the following magic commands for our magic cinema:
show_movies
show_movie_projections <movie_id> [<date>]
make_reservation
cancel_reservation <name>
help
exit
abracadabra""")


def abracadabra():
    print("YOUR COMPUTER IS GOING TO EXPLODE IN 3 SECONDS !!! RUN FOR YOUR LIFE !!!")
    time.sleep(3)
    print("BOOOOOOOM")
    sys.exit()


def show_movies():
    print("Current movies:")
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM Movies ORDER BY rating")
    for row in result.fetchall():
        print(row)


def cancel_reservation(name):  # we have to handle the case where the name is not in reservation table
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Reservations WHERE username = \"{}\"".format(name))
    conn.commit()


def show_movie_projections(movie_id, date=None):  # current function doesn't print the remaining free seats
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()
    if date is None:
        result = cursor.execute("SELECT proj_id, date, time, type FROM projections WHERE movie_id = {} ORDER BY date".format(movie_id))
    else:
        result = cursor.execute("SELECT proj_id, time, type FROM projections WHERE movie_id = {} AND date = {} ORDER BY date".format(movie_id, date))
    for row in result.fetchall():
        print(row)

# Happy coding :)
# ^ ^
# ---
