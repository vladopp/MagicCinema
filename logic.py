import sqlite3

def show_movies():
    conn = sqlite3.connect("Movies.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT rating FROM movies")
    for row in result:
        print(row)
