import logic

while True:
    command = input("command>")
    if command == "show_movies":
        logic.show_movies()
    elif command == "show_movie_projection": # to be fixed
        logic.show_movie_projection(movie_id, date=None)
    elif command == "make_reservation":
        logic.make_reservation()
    elif command == "cancel_reservation":
        logic.cancel_reservation()
    elif command == "help":
        logic.helpp()
    elif command == "abracadabra":
        logic.abracadabra()
    elif command == "exit":
        break
