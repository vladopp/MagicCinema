import sqlite3
import sys
import time

def helpp():
    print("""
You can use the following magic commands for our magic cinema:
show_movies
show_movie_projection
make_reservation
cancel_reservation
help
exit
abracadabra
""")

def abracadabra():
    print("YOUR COMPUTER IS GOING TO EXPLODE IN 3 SECONDS !!! RUN FOR YOUR LIFE !!!")
    time.sleep(3)
    print("BOOOOOOOM")
    sys.exit()


def show_movies():
    conn = sqlite3.connect("Movies.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT name FROM movies ORDER BY rating")
    for row in result:
        print(row)
