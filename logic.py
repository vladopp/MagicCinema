import sqlite3
import sys
import time

CINEMA_DB = "cinema.db"

conn = sqlite3.connect(CINEMA_DB)
cursor = conn.cursor()


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
    print("YOUR COMPUTER IS GOING TO EXPLODE IN 3 SECONDS!!! RUN FOR YOUR LIFE!!!")
    time.sleep(3)
    print("BOOOOOOOM")
    sys.exit()


def show_movies():
    print("Current movies ordered by rating:")
    result = cursor.execute("""
        SELECT id, name
        FROM Movies
        ORDER BY rating DESC
    """)
    for row in result.fetchall():
        print("movie_id: {}".format(row[0]), "movie_name: {}".format(row[1]))


def cancel_reservation(name):  # we have to handle the case where the name is not in reservation table
    cursor.execute("""
        DELETE FROM Reservations
        WHERE username = \"{}\"
    """.format(name))
    conn.commit()


# current function doesn't print the remaining free seats
def show_movie_projections(movie_id, date=None):
    if date is None:
        result = cursor.execute("""
            SELECT proj_id, date, time, type
            FROM Projections
            WHERE movie_id = {}
            ORDER BY date ASC
        """.format(movie_id))
    else:
        result = cursor.execute("""
            SELECT proj_id, time, type
            FROM projections
            WHERE movie_id = {} AND date = \'{}\'
            ORDER BY date ASC
        """.format(movie_id, date))
    for row in result.fetchall():
        print(row)


def make_reservation():
    pass


def close_connection():
    conn.close()

# Happy coding :)
# ^ ^
# ---

# Thank youuu :)
